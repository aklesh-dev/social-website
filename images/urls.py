from django.urls import path
from . import views

app_name = 'images'

urlpatterns = [
    # -- image_create view function path
    path('create/', views.image_create, name='create'),
]
