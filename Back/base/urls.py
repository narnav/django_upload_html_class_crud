from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('', views.index),
    path('imgs/<pk>', views.MyModelView.as_view()),
    path('imgs/', views.MyModelView.as_view()),
    path('students/', views.student_Views.as_view()),
]
