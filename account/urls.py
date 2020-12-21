from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('single/', views.single, name='single'),
    path('contact/', views.contact, name='contact'),
    path('blog/', views.blogs, name='blogs'),
]
