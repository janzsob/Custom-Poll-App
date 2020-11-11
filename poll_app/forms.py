from django import forms
from .models import Poll, Question, Choice
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class CreatePollForm(forms.ModelForm):
    class Meta:
        model = Poll
        fields = ["question", "option1", "option2", "option3"]

class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ["question_text"]
        #widgets = {
        #   "question_text": forms.Textarea(attrs={"rows":1, "cols":60})
        #}
        
class ChoiceForm(forms.ModelForm):
    class Meta:
        model = Choice
        fields = ["choice_text"]

class CustomCreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]