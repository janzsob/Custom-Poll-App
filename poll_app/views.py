from django.shortcuts import render, redirect, get_object_or_404
from .forms import CreatePollForm, QuestionForm, ChoiceForm, CustomCreateUserForm
from .models import Poll, Question, Choice
from django.http import HttpResponse
from django.urls import reverse
from django.forms.formsets import formset_factory
from django.forms import inlineformset_factory
from django.views import generic
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .decorators import unauthenticated_user, allowed_users

# view for rendering home page
"""
def home_view(request):
    polls = Poll.objects.all()
    context = {"polls": polls}
    return render(request, "poll_app/home.html", context)
"""

"""
@login_required(login_url="poll_app:login")
@allowed_users(allowed_roles=["admin"])
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
"""
@login_required(login_url="poll_app:login")
"""
def create_view(request):
    if not request.user.is_authenticated:
        messages.warning(request, 'You have to log in to be allowed creating poll.')
        return redirect("poll_app:login")
        
    ChoiceFormSet = formset_factory(ChoiceForm, min_num=2, extra=1, validate_min=True)
    if request.method == "POST":
        question_form = QuestionForm(request.POST)
        formset = ChoiceFormSet(request.POST)
        if question_form.is_valid() and formset.is_valid():
            if question_form.cleaned_data:
                poll = question_form.save(commit=False)
                poll.author = request.user
                poll.save()
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
class ResultView(generic.DetailView):
    model = Question
    context_object_name = "poll"
    template_name = "poll_app/result.html"

# View for login page
@unauthenticated_user
def login_view(request):
    """
    if request.user.is_authenticated: # Info message, if the user try to log in, when he is logged in
        messages.info(request, 'You are already logged in.')
        return redirect("poll_app:home")    
    """
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect("poll_app:home")
        else:
            messages.info(request, "Username or password is incorrect")

    context = {}
    return render(request, "poll_app/login.html", context)

# View for user logout
def logout_view(request):
    logout(request)
    return redirect("poll_app:login")

# View for register page
def register_view(request):
    if request.user.is_authenticated: # Info message, if the user try to register, when he is logged in
        messages.info(request, 'You already have an account.')
        return redirect("poll_app:home")
    else:
        form = CustomCreateUserForm()
        if request.method == "POST":
            form = CustomCreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get("username")
                messages.success(request, "Account was created for " + user + "!" "\t Now you have to log in.") 
                return redirect("poll_app:login")
        context = {"form": form}
        return render(request, "poll_app/register.html", context)

# View for search results
class SearchResultsView(generic.ListView):
    model = Question
    template_name = "poll_app/search_result.html"
    context_object_name = "results"

    def get_queryset(self):
        query = self.request.GET.get("s")
        object_list = Question.objects.filter(category__icontains=query)
        return object_list

# view for edit poll
def update_poll(request, pk):
    poll = Question.objects.get(id=pk)
    ChoiceInlineFormset = inlineformset_factory(Question, Choice, fields=["choice_text"], max_num=3)
    form = QuestionForm(instance=poll)
    formset = ChoiceInlineFormset(instance=poll)

    if request.method == "POST":
        if poll.author == request.user:
            form = QuestionForm(request.POST, instance=poll)
            formset = ChoiceInlineFormset(request.POST, instance=poll)
            if form.is_valid() and formset.is_valid():
                form.save()
                formset.save()
                return redirect("poll_app:home")
        else:
            messages.warning(request, "You are not entitled to modify the poll because you are not its Author.")

    context = {"form": form, "formset": formset}
    return render(request, "poll_app/edit.html", context)

# View for delet poll

def delete_view(request, pk):
    poll = Question.objects.get(id=pk)
    if request.method == "POST":
        if poll.author == request.user:
            poll.delete()
            return redirect("poll_app:home")
        else:
            messages.warning(request, "You are not entitled to delete the poll because you are not its Author.")    
    context = {"poll": poll}
    return render(request, "poll_app/delete.html", context)