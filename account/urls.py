from django.urls import path
from django.contrib.auth import views as auth_views

from account import views

urlpatterns = [
    # path('login/', views.user_login, name='login')
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('', views.dashboard, name='dashboard'),
    # 비밀번호 변경
    path('password-change/', auth_views.PasswordChangeView.as_view(), name='password_change'),
]
