from django.db import models


# Create your models here.
class Message(models.Model):
    name = models.CharField(max_length=20, verbose_name="姓名", primary_key=True)
    email = models.EmailField(verbose_name="邮箱")
    address= models.CharField(max_length=100, verbose_name="联系地址")
    message = models.TextField(verbose_name="留言信息")

    class Meta:
        verbose_name = verbose_name_plural = "留言信息"
        db_table = "message"