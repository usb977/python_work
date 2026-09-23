from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required    #导入装饰器
from django.http import Http404

from .models import Topic, Entry
from .forms import TopicForm, EntryForm

# Create your views here.

def index(request):
    """学习笔记的主页"""
    return render(request, 'learning_logs/index.html')

@login_required
def topics(request):
    """"显示所有主题的界面"""
    topics = Topic.objects.filter(owner=request.user).order_by('date_added')
    context = {'topics':topics}
    return render(request, 'learning_logs/topics.html', context)

@login_required
def topic(request, topic_id):
    """显示单个主题的界面"""
    topic = Topic.objects.get(id=topic_id)
    if topic.owner != request.user:  #拒绝没有权限的用户访问单个主题页
        raise Http404
    
    entries = topic.entry_set.order_by('-date_added') #减号的意思是按降序排序
    context = {'topic':topic, 'entries':entries}
    return render(request, 'learning_logs/topic.html', context)

@login_required
def new_topic(request):
    """用户新建主题"""
    if request.method != 'POST':
        #未提交数据，就创建一个全新的表单
        form = TopicForm()
    else:
        form = TopicForm(data=request.POST)
        if form.is_valid():
            new_topic = form.save(commit=False)
            new_topic.owner = request.user
            new_topic.save()  #写入数据库
            return redirect('learning_logs:topics')   #如果成功直接结束当前函数并返回结果
    #如果输入为空或者数据无效
    context = {'form':form}
    return render(request, 'learning_logs/new_topic.html', context)

@login_required
def new_entry(request, topic_id):
    """在某个主题中添加新条目"""
    topic = Topic.objects.get(id=topic_id)

    if topic.owner != request.user:
        raise Http404

    if request.method != 'POST':
        #未提交数据，就创建一个全新的表单
        form = EntryForm()
    else:
        form = EntryForm(data=request.POST)
        if form.is_valid():
            new_entry = form.save(commit=False)  #将form表单中有效信息转化为Entry的一个实例
            new_entry.topic = topic
            new_entry.save()
            return redirect('learning_logs:topic',topic_id = topic_id)   #如果成功直接结束当前函数并返回结果
    #如果输入为空或者数据无效
    context = {'topic':topic, 'form':form}
    return render(request, 'learning_logs/new_entry.html', context)

@login_required
def edit_entry(request, entry_id):
    """用户修改具体的条目"""
    entry = Entry.objects.get(id=entry_id)
    topic = entry.topic
    if topic.owner != request.user:  #不允许其他用户通过修改网页查看其他用户的文件
        raise Http404

    if request.method != 'POST':
        #初次GET请求：将当前的条目内容填充到表单中
        form = EntryForm(instance=entry)
    else:
        #已填充好，发送POST
        form = EntryForm(instance=entry, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('learning_logs:topic',topic_id=topic.id)  #只定义了变量topic，所以是topic.id
    #如果数据无效或者首次请求，返回当前页面
    context = {'entry':entry, 'topic':topic, 'form':form}
    return render(request, 'learning_logs/edit_entry.html', context)