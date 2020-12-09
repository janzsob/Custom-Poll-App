from django.urls import path
from . import views

app_name = "vote_app"
urlpatterns = [
    path("details/<int:pk>/", views.DetailView.as_view(), name="details"),
    path("vote/<int:question_id>/", views.vote, name="vote"),
    path("result/<int:pk>/", views.ResultsView.as_view(), name="result")
]