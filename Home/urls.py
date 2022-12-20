from django.urls import path
from .views import *
from Home import views


urlpatterns = [
    path('index/', Index.as_view(), name='index'),
    path('blog/', Blogg.as_view(), name='blog'),
    path('blogadd/', Add_blog.as_view(), name='blogadd'),
    path('inforadd/', Inforadd.as_view(), name='inforadd'),
    path('servisadd/', Servisadd.as_view(), name='servisadd'),
    path('popadd/', Popuadd.as_view(), name='popadd'),
    path('about/', About.as_view(), name='about'),
    path('like/<int:pk>/', views.like, name='like'),
    # path('delete/<int:pk>/', Delet.as_view(), name='delet'),
    path('dis/<int:pk>/', Distin.as_view(), name='dis'),
    path('popular/', Popular.as_view(), name='popular'),
]