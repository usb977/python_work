from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm

# Create your views here.

def register(request):
    """注册新用户"""
    if request.method != 'POST':
        #首次点注册是空表单，这个时候发送的GET请求
        form = UserCreationForm()
    else:
        #处理填好的表单
        form = UserCreationForm(data=request.POST)

        if form.is_valid():
            new_user = form.save()
            #让用户自动登录，再重定向到主页
            login(request, new_user)
            return redirect('learning_logs:index')
    #显示空表单或者指出表单无效
    context = {'form':form}
    return render(request, 'registration/register.html', context)