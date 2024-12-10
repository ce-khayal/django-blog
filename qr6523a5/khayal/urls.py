from django.contrib import admin
from django.urls import path,include
from khayal import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    path("user/<str:name>/<int:age>", views.user),
    path('about/', views.about),
    path('contact/', views.contact),
    path('cats/',views.categories,kwargs={'name':'Khayal','age':'19'}),
    path('user1/',views.user1),
    path('sablon/',views.sablon),
    path('sablon2',views.yeni)
]