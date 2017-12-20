from django.urls import path
from . import views


urlpatterns = [
    path('', views.vessem, name='vessem'),
    path('post/(?P<pk>\d+)/', views.post_detail, name='post_detail'),
    path('post/new/', views.post_new, name='post_new'),
]