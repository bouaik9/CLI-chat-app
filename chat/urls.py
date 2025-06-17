from django.urls import path
from . import views

urlpatterns = [
    path('rooms/', views.room_list, name='room_list'),
    path('rooms/<slug:slug>/', views.room_detail, name='room_detail'),
    path('send_message/', views.send_message, name='send_message'), 
    path('login/', views.login_view, name='login'),
    path('fetch_messages/<slug:slug>/', views.fetch_messages, name='fetch_messages'),
]