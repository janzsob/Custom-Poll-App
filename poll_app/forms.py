from django import forms
from .models import Poll, Question, Choice


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