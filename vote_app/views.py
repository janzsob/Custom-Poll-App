from django.shortcuts import render, get_object_or_404, HttpResponse, HttpResponseRedirect
from .models import Question, Choice
from django.urls import reverse
from django.views import generic


"""
def detail(request, question_id):
    req_question = get_object_or_404(Question, pk=question_id)
    return render(request, "vote_app/details.html", {"req_question": req_question})
"""
class DetailView(generic.DetailView):
    model = Question
    context_object_name = "req_question"
    template_name = "vote_app/details.html"

def vote(request, question_id):
    req_question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = req_question.choice_set.get(pk=request.POST["choice"])
    except(KeyError, Choice.DoesNotExist):
        return render(request, "vote_app/vote.html", {
            "req_question": req_question, 
            "error_message": "You haven't voted"
            })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse("vote_app:result", args=(req_question.id,)))


"""
def results(request, question_id):
    req_result = get_object_or_404(Question, pk=question_id)
    return render(request, "vote_app/results.html", {"req_result": req_result})
"""
class ResultsView(generic.DetailView):
    model = Question
    context_object_name = "req_result"
    template_name = "vote_app/results.html"
