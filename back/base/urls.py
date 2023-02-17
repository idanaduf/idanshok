from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('', views.index),
    path('about/', views.about),
    path('login/', views.MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('logout', views.LogoutAPIView.as_view(), name='logout'),
    path('register/',views.register ),
    path('myProducts/', views.myProducts),
    path('clients/', views.clients),
    path('get_all_images', views.getImages),
    path('upload_image/',views.APIViews.as_view()),
    path('refresh',views.RefreshTokenView.as_view(),name='refresh_token'),





]
