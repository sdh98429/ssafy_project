from django.core import paginator
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework.serializers import Serializer

from .models import Genre, Movie, Review
from .serializers import  MovieSerializer, ReviewSerializer, GenreSerialzer
import requests
import json

# 영화 전체 리스트
@api_view(['GET'])
@permission_classes([AllowAny])
def movie_list(request):
    movies = Movie.objects.all()
    serializer = MovieSerializer(movies, many=True)
    return Response(serializer.data)

# 장르 수집
@api_view(['GET'])
def movie_genre(request):
    genres = Genre.objects.all()
    serializer = GenreSerialzer(genres, many=True)
    return Response(serializer.data)

# 영화 정보
@api_view(['GET'])
def movie_detail(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    serializer = MovieSerializer(movie)
    return Response(serializer.data)

# 영화 추천
# 1. top rated
# 2. 장르
# 3. 태그로 영화 추천 (비오는 날 보기 좋은 영화 == 공포, 스릴러)

API_KEY = '023789149b726b1e45b32354922160c6'
BASE_URL = 'https://api.themoviedb.org/3'

@api_view(['GET'])
@permission_classes([AllowAny])
def recommend_movie(request):
    movies = Movie.objects.all()
    serializer = MovieSerializer(movies, many=True)
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes([AllowAny])
def search(request):
    movies = Movie.objects.all()
    serializer = MovieSerializer(movies, many=True)
    return Response(serializer.data)



# 현재 상영중인 영화
@api_view(['GET'])
@permission_classes([AllowAny])
def nowplaying(request):
    res = requests.get(f'{BASE_URL}/movie/now_playing?api_key={API_KEY}&language=ko-KR&page=1')
    movies = res.json().get('results')
    data = []
    for i in movies:
        movie = {
            "movie_id": i.get("id"), 
            "title": i.get('title'),
            "release_date": i.get('release_date'),
            "popularity": i.get('popularity'),
            "vote_count": i.get('vote_count'),
            "vote_average": i.get('vote_average'),
            "overview": i.get('overview'),
            "poster_path": i.get('poster_path'),
            "genres": i.get('genre_ids')
        }
        data.append(movie)
    return Response(data)

# top rated(1)
@api_view(['GET'])
@permission_classes([AllowAny])
def popular(request):
    movies = Movie.objects.all().order_by('-popularity')
    serializer = MovieSerializer(movies, many=True)
    return Response(serializer.data)

#평점이 높은 영화 순서
@api_view(['GET'])
@permission_classes([AllowAny])
def voteaverage(request):
    movies = Movie.objects.filter(vote_average__gt = 0).order_by('-vote_average')
    serializer = MovieSerializer(movies, many=True)
    return Response(serializer.data)


# 리뷰 생성
@api_view(['POST'])
def create_review(request, movie_pk):
    if request.user.is_authenticated:
        movie = get_object_or_404(Movie, pk=movie_pk)
        review = Review(
            content=request.data.get('content'),
            like = request.data.get('like'),
            rate = request.data.get('rate'),
            user = request.user,
            movie = movie,
        )
        review.save()
        serializer = ReviewSerializer(review)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


# 리뷰 제공
@api_view(['GET'])
@permission_classes([AllowAny])
def review_list(request, movie_pk):
    reviews = Review.objects.all().filter(movie_id=movie_pk)
    serializer = ReviewSerializer(reviews, many=True)
    return Response(serializer.data)

# 리뷰 수정, 삭제 
@api_view(['PUT', 'DELETE'])
def review_update_or_delete(request, review_pk, movie_pk):
    review = get_object_or_404(Review, pk=review_pk)
    movie = get_object_or_404(Movie, pk=movie_pk)


    if request.user != review.user:
        return Response({'detail', '권한이 없습니다.'}, status=status.HTTP_400_BAD_REQUEST)
        

    if request.method == 'PUT':
        review = get_object_or_404(Review, pk=review_pk)
        serializer = ReviewSerializer(review, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            print("----update error", serializer.errors)


    
    else:
        review.delete()
        return Response({'id': review_pk}, status=status.HTTP_204_NO_CONTENT)
    


