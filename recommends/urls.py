from django.urls import path
from . import views

app_name = 'buk2on_on'
urlpatterns = [
    path('', views.index , name='index'),
    path('<int:restaurant_pk>/', views.detail , name='detail'),
    path('create/', views.create, name = 'create'),
    # path('<int:restaurant_pk>/update/', views.update, name = 'update'),
    path('<int:restaurant_pk>/delete/', views.delete, name = 'delete'),
    path('seoul/', views.seoul_main , name = 'seoul_main'),
    path('busan/', views.busan_main , name = 'busan_main'),
    path('etc/', views.etc_main , name = 'etc_main'),
    path('<int:restaurant_pk>/comments/', views.comments_create , name = 'comments_create'),
] 