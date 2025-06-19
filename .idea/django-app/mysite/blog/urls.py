from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('feedback/', views.feedback_view, name='feedback'),
    path('books/', views.book_list, name='books_list'),
    path('articles/', views.article_list, name='articles_list'),
]