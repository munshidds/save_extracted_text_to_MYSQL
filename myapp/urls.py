from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.upload_image, name='upload_image'),
    path('display/', views.display_image, name='display_image')
]
