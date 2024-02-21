from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path(
        'detailed_post/<slug:slug>', 
        views.detailed_post, 
        name='detailed_post'),
    
]