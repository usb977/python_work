from django import forms
from .models import Topic,Entry

class TopicForm(forms.ModelForm):
    class Meta:
        model = Topic   #根据Topic模型来创建表单
        fields = ['text']
        labels = {'text':''} #不要创建标签

class EntryForm(forms.ModelForm):
    class Meta:
        model = Entry   #根据Entry模型来创建表单
        fields = ['text']
        labels = {'text':''}  #不要创建标签
        widgets = {'text':forms.Textarea(attrs={'cols':80})}  #widgets是自定义字段显示方式，把 text 这个字段从默认的单行输入框，改成宽度为 80 列的多行文本框
