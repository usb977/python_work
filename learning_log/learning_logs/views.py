from django.shortcuts import render

from .models import Topic

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
