from django.urls import path
from app import views

urlpatterns=[
    path('',views.login,name='login'),
    path('register/',views.register,name='register'),
    path('library_management/',views.library_management,name='library_management'),
    path('member_management/',views.member_management,name='member_management'),

]