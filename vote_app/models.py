from django.db import models
from django.utils.timezone import now

class Question(models.Model):
    question_text = models.CharField(max_length=300)
    publish_date = models.DateTimeField(default=now)

    def __str__(self):
        return self.question_text

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=300)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text