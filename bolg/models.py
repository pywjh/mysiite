from django.db import models

# Create your models here.

class BlogModel(models.Model):
    title = models.CharField(max_length=100,unique=True)
    content = models.TextField()
    update_time = models.DateTimeField(auto_now=True) # 更新时间，多次
    create_time = models.DateField(auto_now_add=True) # 只填写一次的时间
    def __str__(self):
        return 'BlogModel<id=%s, title=%s, content=%s>'%(
            self.id, self.title, self.content
        )