from django.contrib import admin
from django.urls import path
from tienda import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    path('mause/', views.mause),
    path('teclado/', views.teclado),
    path('casco/', views.casco),

]