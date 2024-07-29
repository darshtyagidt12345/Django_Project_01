from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add/', views.add, name='add'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('update/', views.update, name='update'),
    path('delete/', views.delete, name='delete'),
    path('login/', views.loginUser, name='loginUser'),
    path('logout/', views.logoutUser, name='logout'),
    path('view/', views.viewall, name='view'),
    #user-darshtyagidt15 pass-abc123def456
    #user-DarshTyagi1234 pass-password
]
