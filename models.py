from django.db import models
from django.utils.timezone import now


class Article(models.Model):
    title = models.CharField('标题', max_length=200)
    source = models.CharField('来源', max_length=100)
    date = models.DateTimeField('日期',default=now)
    content = models.TextField('内容')

    def __str__(self):
        return self.title

