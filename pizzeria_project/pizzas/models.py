from django.db import models

# Create your models here.

class Pizza(models.Model):
    """定义pizza种类"""
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)
        
    def __str__(self):
        """返回模型的字符串表示"""
        return self.text

class Toppings(models.Model):
    """配料表"""
    topic = models.ForeignKey(Pizza, on_delete=models.CASCADE) #外键，指向另一台记录，即关联到Topic；级联删除
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text
