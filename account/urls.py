from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='index'),
    path('single/', views.single, name='single'),
    path('contact/', views.contact, name='contact'),
    path('blog/', views.blogs, name='blogs'),
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
