"""定义learning_logs的URL模式"""

from django.urls import path
from . import views

app_name = 'learning_logs'

urlpatterns = [
    path('', views.index, name='index'), #定义主页url的视图
    path('topics/', views.topics, name='topics'), #定义显示所有主题页面的视图
    path('topics/<int:topic_id>/', views.topic, name='topic'), #某个特定主题的视图
    path('new_topic/', views.new_topic, name='new_topic'), #用户新建主题的跳转
    path('new_entry/<int:topic_id>/', views.new_entry, name='new_entry'), #用户新建条目的跳转
]