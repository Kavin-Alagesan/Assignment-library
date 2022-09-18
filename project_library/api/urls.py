from django.urls import path
from .views import *
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns=[
    path('create_user/', UserCreate.as_view()),
    path('update_user/<int:pk>/',UserUpdateDelete.as_view()),
    path('create_book/',BookCreate.as_view()),
    path('update_user/<int:pk>/', BookUpdateDelete.as_view()),
    path('token/',TokenObtainPairView.as_view()),
    path('token/refresh/',TokenRefreshView.as_view()),
    path('login/', LoginView.as_view()),
    path('logout/', Logout.as_view()),

]
