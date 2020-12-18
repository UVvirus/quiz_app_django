from django.urls import path
from . import views

urlpatterns=[
    path('',views.index,name='index'),
    path('<int:pk>/detail/',views.detail,name='detail'),
    path('?P<question_id>[0-9]/results/',views.results,name='result'),


]