from django.urls import path
from . import views

urlpatterns = [
	path('', views.index, name=''),
	path('chat/<str:room_name>/', views.room, name='room'),
	path('chattemplate',  views.chattemplate)
]