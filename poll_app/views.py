from django.shortcuts import render, redirect
from .forms import CreatePollForm
from .models import Poll
from django.http import HttpResponse
from django.urls import reverse

# view for rendering home page
def home_view(request):
    polls = Poll.objects.all()
    context = {"polls": polls}
    return render(request, "poll_app/home.html", context)

# view for creating poll
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

# view for vote
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

# view for results
def result_view(request, poll_id):
    poll = Poll.objects.get(pk=poll_id)
    context = {"poll": poll}
    return render(request, "poll_app/result.html", context)