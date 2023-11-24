from django.urls import path
from diaryApp import views

urlpatterns = [
    path('', views.diary_index),
    path('delete/<id>/', views.diary_delete),
    path('update1/<id>/', views.diary_update),
    path('create/', views.diary_create),
]
