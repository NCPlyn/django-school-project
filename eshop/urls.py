from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('sestavy/', views.SestavaListView.as_view(), name='sestavy'),
    path('sestavy/<int:pk>/', views.SestavaDetailView.as_view(), name='sestava_detail'),
]