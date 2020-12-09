from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.views.generic import CreateView
from .models import VoteQuestion, VoteChoice
from .forms import VoteQuestionForm, VoteChoiceForm


"""
# View for creating vote panel
def create_vote(request):
    if request.method == "POST":
        form = VotePanelForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("Thank you for your vote!")
    else:
        form = VotePanelForm()
    return render(request, "voting_panel/create_vote_panel.html", {"form": form})

"""

"""
# Generic view for creating vote panel
class CreateVote(CreateView):
    model = VotePanel
    template_name = "voting_panel/create_vote_panel.html"
    fields = ["question_text", "choice1", "choice2", "choice3", "choice4"]
"""

# View for display vote panel
def panel_view(request, question_id):
    panel = get_object_or_404(VoteQuestion, pk=question_id)
    return render(request, "voting_panel/panel_results.html", {"panel": panel})

# View for create new voting panel (2 models are applied)
def create_panel_view(request):
    if request.method == "POST":
        question_form = VoteQuestionForm(request.POST)
        choice_form = VoteChoiceForm(request.POST)

        if question_form.is_valid() and choice_form.is_valid():
            question_form.save()
            choice_form.save()
            return HttpResponse("Vote was submitted!")

    else:
        question_form = VoteQuestionForm()
        choice_form = VoteChoiceForm()

    context = {
        "question_form": question_form,
        "choice_form": choice_form,
    }
    return render(request, "voting_panel/create_vote_panel.html", context)