# Create your models here.
from django.db import models
from django.utils import timezone

class Post(models.Model):  #定义一个对象，模型名字，表明Post是一个Django模型
    author = models.ForeignKey('auth.User',on_delete=models.CASCADE) #指向另一个模型的连接
    title = models.CharField(max_length=200)  #有限字符
    text = models.TextField() #没有长度限制的文本
    created_date = models.DateTimeField(  #时间和日期
        default = timezone.now)
    published_date = models.DateTimeField(
        blank=True,null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def _str_(self):
        return self.title