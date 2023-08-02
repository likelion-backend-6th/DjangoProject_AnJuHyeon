from django.urls import path
from . import views

# 앱 이름을 'images'로 정의합니다.
app_name = 'images'

# URL 패턴을 설정합니다.
urlpatterns = [
    path('create/', views.image_create, name='create'),
]