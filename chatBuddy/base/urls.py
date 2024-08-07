from django.urls import path
from . import views

urlpatterns = [
     path('login/', views.loginPage, name='login'),
     path('', views.room, name="room"),
     path('room/<str:pk>/', views.home, name="home"),
     path('create-room/', views.createRoom, name="create-room"),

     path('update-room/<str:pk>/', views.updateRoom, name="update-room"),
     path('delete-room/<str:pk>/', views.deleteRoom, name="delete-room"),
     path('create-room/', views.createRoom, name="create-room"),
     path('delete-message/<str:pk>/', views.deleteMessage, name="delete-message"),

     path('topics/', views.topicsPage, name="topics"),
     path('activity/', views.activityPage, name="activity"),
]