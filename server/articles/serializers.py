from rest_framework import serializers
from .models import Article, Comment
from django.contrib.auth import get_user_model

class UserInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ('id', 'username')

class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        # fields = ('title', 'category', 'image', 'content',)
        fields = ('id', 'title', 'content', 'user', 'created_at',)

class ArticleUserSerializer(serializers.ModelSerializer):
    user = UserInfoSerializer()
    class Meta:
        model = Article
        fields = ('id','user','title','content','created_at','updated_at')

class CommentSerializer(serializers.ModelSerializer):
    user = UserInfoSerializer()
    class Meta:
        model = Comment
        fields = ('id', 'content', 'article', 'user', 'created_at',)

