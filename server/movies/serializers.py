from rest_framework import serializers
from .models import Movie, Genre, Review
from django.contrib.auth import get_user_model

class GenreSerialzer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = '__all__'

class MovieSerializer(serializers.ModelSerializer):
    genres = GenreSerialzer(many=True)
    class Meta:
        model = Movie
        fields = '__all__'

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        # fields =  '__all__'
        fields = ('id', 'content', 'movie', 'user', 'rate', 'like',)


