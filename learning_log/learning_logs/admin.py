from django.contrib import admin

# 在这里注册你的模型

from .models import Topic, Entry
admin.site.register(Topic)  #在管理页面注册Topic模型
admin.site.register(Entry)  #在管理页面注册Entry模型
