from django.db import models

# Create your models here.
class Question(models.Model):
    question=models.CharField(max_length=80)
    date_of_publication=models.DateTimeField()

    def __str__(self):
        return self.question


class Options(models.Model):
    ques=models.ForeignKey(Question,on_delete=models.CASCADE)
    """"
    CASCADE: When the referenced object is deleted, also
    delete the objects that have references  to it
    """""
    options=models.CharField(max_length=40)

    def __str__(self):
        return self.options