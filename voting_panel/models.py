from django.db import models

"""
class VotePanel(models.Model):
    question_text = models.CharField(max_length=300)
    choice1 = models.CharField(max_length=200)
    choice2 = models.CharField(max_length=200)
    choice3 = models.CharField(max_length=200, blank=True)
    choice4 = models.CharField(max_length=200, blank=True)
    
    def __str__(self):
        return self.question_text

"""
class VoteQuestion(models.Model):
    question_text = models.CharField(max_length=300)
    theme = models.CharField(max_length=200)

    def __str__(self):
        return self.question_text


class VoteChoice(models.Model):
    question = models.ForeignKey(VoteQuestion, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text