from django.urls import path

from . import views
from . import views
app_name = "roll_call"


urlpatterns = [
    path('', views.floor_list, name='floor_list'),#모든 층 출력
    path('floor/ans/<int:pk>/', views.floor_ans, name='ans'), #층의 무단 외박자
    path('floor/roll_call/<int:pk>/', views.roll_call, name='roll_call'),# 점호를 하는 것
    path('floor/ans_all/', views.ans_all, name='ans_all'),#전체 층 무단 외박자

]
