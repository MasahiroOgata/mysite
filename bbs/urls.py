from django.urls import path
from . import views

app_name = 'bbs'

urlpatterns = [
    path('', views.index, name='index'),    
    path('new', views.new, name='new'),
    path('create', views.create, name='create'),
    path('<str:id>', views.detail, name='detail'),
    path('<str:id>/edit', views.edit, name='edit'),
    path('<str:id>/update', views.update, name='update'),
    path('<str:id>/delete', views.delete, name='delete'),
]