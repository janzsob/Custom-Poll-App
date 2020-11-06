from django.db import models

class Poll(models.Model):
    question = models.TextField()
    option1 = models.CharField(max_length=100)
    option2 = models.CharField(max_length=100)
    option3 = models.CharField(max_length=100)
    option1_votes = models.IntegerField(default=0)
    option2_votes = models.IntegerField(default=0)
    option3_votes = models.IntegerField(default=0)

    def total(self):
        return self.option1_votes + self.option2_votes + self.option3_votes

    def __str__(self):
        return self.question

class Question(models.Model):
    question_text = models.TextField("Question", max_length=300)

    def __str__(self):
        return self.question_text

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField("Choice",max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text