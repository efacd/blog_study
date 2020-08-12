from django.db import models

# Create your models here.
class Post(models.Model):
    author = models.CharField('작성자', max_length=20)
    contents = models.TextField('내용', max_length=1000)
    create_date = models.DateField

    def __str__(self):
        return self.contents

class Tag(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    author = models.CharField('댓글작성자', max_length=20)
    contents = models.TextField('댓글내용', max_length=100)

    def __str__(self):
        return self.contents