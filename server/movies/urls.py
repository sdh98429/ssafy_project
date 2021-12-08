from django.urls import path
from . import views


urlpatterns = [
    path('', views.movie_list),
    path('genre/', views.movie_genre),
    path('<int:movie_pk>/', views.movie_detail),
    path('recommend/', views.recommend_movie),
    path('<int:movie_pk>/reviews/', views.review_list),
    path('<int:movie_pk>/reviews/add', views.create_review),
    path('<int:movie_pk>/reviews/<int:review_pk>/', views.review_update_or_delete),
    path('nowplaying/', views.nowplaying),
    path('popular/', views.popular),
    path('search/', views.search),
    # path('random/', views.random),
]