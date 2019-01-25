from django.urls import path

from . import views

app_name = 'article'

urlpatterns = [
    path('dashboard/', views.dashboard, name='dashboard'),
    path('addarticle/', views.addarticle, name='addarticle'),
    path('update/<int:id>', views.update, name='update'),
    path('delete/<int:id>', views.delete, name='delete'),
    path('detail/<int:id>', views.detail, name='detail'),
    path('addcomment/<int:id>', views.addcomment, name='addcomment'),


]
