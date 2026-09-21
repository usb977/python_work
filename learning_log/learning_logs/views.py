from django.shortcuts import render,redirect

from .models import Topic
from .forms import TopicForm, EntryForm

# Create your views here.

def index(request):
    """学习笔记的主页"""
    return render(request, 'learning_logs/index.html')

def topics(request):
    """"显示所有主题的界面"""
    topics = Topic.objects.order_by('date_added')    #列表项按照创建时间从先到后
    context = {'topics':topics}
    return render(request, 'learning_logs/topics.html', context)

def topic(request, topic_id):
    """显示单个主题的界面"""
    topic = Topic.objects.get(id=topic_id)
    entries = topic.entry_set.order_by('-date_added') #减号的意思是按降序排序
    context = {'topic':topic, 'entries':entries}
    return render(request, 'learning_logs/topic.html', context)

def new_topic(request):
    """用户新建主题"""
    if request.method != 'POST':
        #未提交数据，就创建一个全新的表单
        form = TopicForm()
    else:
        form = TopicForm(data=request.POST)
        if form.is_valid():
            form.save()  #写入数据库
            return redirect('learning_logs:topics')   #如果成功直接结束当前函数并返回结果
    #如果输入为空或者数据无效
    context = {'form':form}
    return render(request, 'learning_logs/new_topic.html', context)

def new_entry(request, topic_id):
    """在某个主题中添加新条目"""
    topic = Topic.objects.get(id=topic_id)

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