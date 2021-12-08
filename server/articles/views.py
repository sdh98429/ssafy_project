
from django.db.models.fields.related import RECURSIVE_RELATIONSHIP_CONSTANT
from django.shortcuts import get_object_or_404

from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny

from .serializers import ArticleSerializer, CommentSerializer, ArticleUserSerializer
from .models import Article, Comment

@api_view(['GET', 'POST'])
@permission_classes([AllowAny])
def article_list_create(request):
    if request.method == 'GET':
        articles = Article.objects.all()
        serializer = ArticleUserSerializer(articles, many = True)
        return Response(serializer.data)
    else:
        articleItem = request.data
        print("=============", request.user)
        article = Article(
            user = request.user,
            title = articleItem['title'],
            content = articleItem['content'],
            # image = articleItem['image']
        )
        article.save()
        serializer = ArticleUserSerializer(article)

        return Response(serializer.data)

        # print('what')
        # print(request.data)
        # serializer = ArticleSerializer(data=request.data)
        # print(serializer)
        # if serializer.is_valid(raise_exception=True):
        #     serializer.save(user=request.user)
        #     print('who', request.user)
        #     return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['PUT', 'DELETE'])
def article_update_delete(request, article_id):
    article = get_object_or_404(Article, pk=article_id)

    if not request.user.articles.filter(pk=article_id).exists():
        return Response({'detail', '권한이 없습니다.'}, status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'PUT':
        if not request.data:
            return Response(True)
        request.data['user'] = request.user.pk
        serializer = ArticleSerializer(article, data=request.data)
        print(serializer)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
        else:
            print("----update error", serializer.errors)
        return Response(serializer.data)
    
    else:
        article.delete()
        return Response({'id': article_id}, status=status.HTTP_204_NO_CONTENT)

@api_view(['GET'])
@permission_classes([AllowAny])
def article_detail(request, article_id):
    article = get_object_or_404(Article, id=article_id)
    serializer = ArticleUserSerializer(article)
    return Response(serializer.data)


@api_view(['GET', 'POST'])
@permission_classes([AllowAny])
def article_detail_comment_list_create(request, article_id):
    article = get_object_or_404(Article, pk=article_id)

    if request.method == 'POST':
        comment = Comment(content=request.data.get('content'), article=article, user=request.user)
        comment.save()
        serializer = CommentSerializer(comment) # serializer.is_valid() 등의 형식을 쓰면 오류남

        return Response(serializer.data, status=status.HTTP_201_CREATED)


    else:
        comments = Comment.objects.filter(article_id=article_id)
        serializer = CommentSerializer(comments, many=True)
        # print(serializer)
        return Response(serializer.data)

@api_view(['DELETE'])
def article_detail_comment_delete(request, article_id, comment_id):
    
    comment = get_object_or_404(Comment, pk=comment_id)
    if request.method == 'DELETE':
        if request.user == comment.user:
            comment.delete()
            return Response(status.HTTP_204_NO_CONTENT)
