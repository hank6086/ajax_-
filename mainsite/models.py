from django.db import models
from django.utils import timezone
import json
# Create your models here.


class testPost(models.Model):
    title = models.CharField(max_length=200)
    slug = models.CharField(max_length=200)
    body = models.TextField()
    pub_data = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ('-pub_data', )

    def __str__(self):
        teststr = '{0}:{2}'.format(self.title, self.slug, self.body)
        teststr = teststr.strip('[') + "ismydata"
        return teststr


class post2(models.Model):
    stname = models.CharField(max_length=10)
    number = models.CharField(max_length=3)
    time = models.DateTimeField(default=timezone.now)

    def __str__(self):
        # test = dict()
        test = {
            'stname': self.stname,
            'number': self.number,
            'time': str(self.time)
        }
        return str(test)


    # def __str__(self):
    #         teststr ='{0}:{2}'. format(self.stname ,self.number , self.time)
    #         return teststr
class id_ap(models.Model):
    idname = models.CharField(max_length=30)
    uid = models.CharField(max_length=50, default="")
    def __str__(self):
        users = dict
        users = {
            'idname':self.idname,
            'uid':self.uid
        }
        return str(users)
    # class Meta:
    #     db_table ='id_ap'


class megall(models.Model):
    meg_text = models.TextField()
    user_uid = models.CharField(max_length=50, default="")
    text = dict()
    def __str__(self):
        text = {
            'meg': self.meg_text,
            'uid':self.user_uid
        }
        return str(text)