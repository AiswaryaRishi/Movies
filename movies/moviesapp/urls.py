from django.urls import path, include
from . import views

app_name = 'moviesapp'
urlpatterns = [
    path('', views.index, name='index'),
    path('movie/<int:mid>/', views.detail, name='detail'),
    path('add/', views.addmovie, name='addmovie'),
    path('update/<int:id>/', views.update, name='update'),
    path('delete/<int:id>/', views.delete, name='delete')

]
