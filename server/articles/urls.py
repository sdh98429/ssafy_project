from django.urls import path
from . import views

app_name = 'article'

urlpatterns = [
    path('', views.article_list_create),
    path('<int:article_id>/', views.article_detail),
    path('<int:article_id>/update_delete/', views.article_update_delete),
    path('<int:article_id>/comments/', views.article_detail_comment_list_create),
    path('<int:article_id>/comments/<int:comment_id>', views.article_detail_comment_delete),


    # path('', views.index, name='index'),
    # path('create/', views.create, name='create'),
    # path('<int:article_pk>/', views.detail, name='detail'),
    # path('<int:article_pk>/comments/create', views.create_comment, name='create_comment'),
    # path('<int:article_pk>/like/', views.like, name='like'),
]