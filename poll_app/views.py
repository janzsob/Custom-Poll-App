from django.shortcuts import render, redirect, get_object_or_404
from .forms import CreatePollForm, QuestionForm, ChoiceForm
from .models import Poll, Question, Choice
from django.http import HttpResponse
from django.urls import reverse
from django.forms.formsets import formset_factory
from django.views import generic

# view for rendering home page
"""
def home_view(request):
    polls = Poll.objects.all()
    context = {"polls": polls}
    return render(request, "poll_app/home.html", context)
"""
def home_view(request):
    polls = Question.objects.all()
    context = {"polls": polls}
    return render(request, "poll_app/home.html", context)

# view for creating poll
"""
def create_view(request):
    if request.method == "POST":
        form = CreatePollForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("poll_app:home")
    else:
        form = CreatePollForm()

    context = {"form": form}
    return render(request, "poll_app/create.html", context)
"""
def create_view(request):
    """
    https://stackoverflow.com/questions/28054991/combining-two-forms-in-one-django-view
    """
    ChoiceFormSet = formset_factory(ChoiceForm, extra=1, min_num=2, validate_min=True)
    if request.method == "POST":
        question_form = QuestionForm(request.POST)
        formset = ChoiceFormSet(request.POST)
        if question_form.is_valid() and formset.is_valid():
            poll = question_form.save()
            for inline_form in formset:
                if inline_form.cleaned_data:
                    choice = inline_form.save(commit=False)
                    choice.question = poll
                    choice.save()
            return redirect("poll_app:home")
    else:
        question_form = QuestionForm()
        formset = ChoiceFormSet()
    
    context = {
        "question_form": question_form,
        "formset": formset
    }
    return render(request, "poll_app/create.html", context)

"""
# view for vote with one model
def vote_view(request, poll_id):
    poll = Poll.objects.get(pk=poll_id)

    if request.method == "POST":
        selected_option = request.POST["poll"]
        if selected_option == "option1":
            poll.option1_votes += 1
        elif selected_option == "option2":
            poll.option2_votes += 1
        elif selected_option == "option3":
            poll.option3_votes += 1
        else:
            return HttpResponse(400, "Invalid form")
        poll.save()
        return redirect(reverse("poll_app:result", args=(poll.id,)))
        
    context = {"poll": poll}
    return render(request, "poll_app/vote.html", context)
"""
# View for vote with multiple models
"""
def vote_view(request, poll_id):
    poll = get_object_or_404(Question, pk=poll_id)
    try:
        selected_choice = poll.choice_set.get(pk=request.POST["choice"])
    except(KeyError, Choice.DoesNotExist):
        return render(request, "poll_app/vote.html", {
            "poll": poll, 
            "error_message": "You haven't voted"
            })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse("poll_app:result", args=(poll.id,)))
"""
def vote_view(request, poll_id):
    poll = get_object_or_404(Question, pk=poll_id)
    if request.method == "POST":
        try:
            selected_choice = poll.choice_set.get(pk=request.POST["clap"])
            print("Oké")    
        except(KeyError):
            return render(request, "poll_app/vote.html", {
                "poll": poll, 
                "error_message": "You haven't voted yet!"
                })
        else:
            selected_choice.votes += 1
            selected_choice.save()
            return redirect(reverse("poll_app:result", args=(poll.id,)))
    else:
        context = {"poll": poll}
        return render(request, "poll_app/vote.html", context)

"""
# view for results with one model
def result_view(request, poll_id):
    poll = Poll.objects.get(pk=poll_id)
    context = {"poll": poll}
    return render(request, "poll_app/result.html", context)
"""
"""
# view for results with multiple models
def result_view(request, poll_id):
    poll = Question.objects.get(pk=poll_id)
    context = {"poll": poll}
    return render(request, "poll_app/result.html", context)
"""
# View for results. Same as above
class ResultView(generic.DeleteView):
    model = Question
    context_object_name = "poll"
    template_name = "poll_app/result.html"