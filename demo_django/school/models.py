from django.db import models


# Create your models here.


class student(models.Model):
    class Meta:
        verbose_name = '学生'
        verbose_name_plural = '学生'
    name = models.CharField('姓名', max_length=50, null=False)
    sex = models.CharField('性别', max_length=2, null=False)
    born = models.DateField('生日', null=False)
    city = models.CharField('城市', max_length=100, null=False)
    like = models.CharField('爱好', max_length=100)
