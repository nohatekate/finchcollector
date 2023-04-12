from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('quarters/', views.quarters_index, name='index'),
    path('quarters/<int:quarter_id>/', views.quarters_detail, name='detail')
]