from django.db import models
from django.utils.timezone import now
from datetime import datetime
from django.contrib.auth.models import User


class Question(models.Model):
    question_text = models.TextField("Question", max_length=300)
    category = models.CharField(max_length=100)
    pupblish_date = models.DateTimeField(default=now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.question_text

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField("Choice",max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text

class Vote(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    voter = models.ForeignKey(User, on_delete=models.CASCADE)