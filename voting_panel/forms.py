from django import forms
from .models import VoteQuestion, VoteChoice

"""

class VotePanelForm(forms.ModelForm):
    class Meta:
        model = VotePanel
        fields = ["question_text", "choice1", "choice2", "choice3", "choice4"]

"""

"""
https://stackoverflow.com/questions/27968417/django-form-with-fields-from-two-different-models
"""
class VoteQuestionForm(forms.ModelForm):
    class Meta:
        model = VoteQuestion
        fields = ["question_text", "theme"]

class VoteChoiceForm(forms.ModelForm):
    class Meta:
        model = VoteChoice
        fields = ["choice_text"]

