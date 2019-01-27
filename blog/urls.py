from django.contrib import admin
from django.urls import path, include

from article import views
#from user import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('contact/', views.contact, name='contact'),
    path('articles/', views.articles, name='articles'),
    path('', views.index, name='index'),
    path('admin/', admin.site.urls),
    path('articles/', include('article.urls')),
    path('users/', include('user.urls')),
    path('todos/', include('todo.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
