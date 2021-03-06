from django.urls import path
from . import views

app_name = 'board'

urlpatterns = [
	path('', views.index, name="index"),
	path('<int:board_id>/detail/', views.detail, name="detail"),

	path('create/', views.create, name="create"),

	path('<int:board_id>/update/', views.update, name="update"),

	path('<int:board_id>/delete/', views.delete, name="delete"),
]