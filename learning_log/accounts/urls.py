"""定义app accounts的URL模式"""

from django.urls import path,include
from . import views

app_name = 'accounts'

urlpatterns = [
    #导入include，这样可以使用django自带的身份验证URL
    path('', include('django.contrib.auth.urls')),  #如accounts/XXX格式的URL都交给后面这个文件解析，因为login、logout有定义所以直接复用
    path('register/', views.register, name='register'),  #注册页面
]