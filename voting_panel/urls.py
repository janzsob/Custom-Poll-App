from django.urls import path
from . import views

app_name = "voting_panel"
urlpatterns = [
    path("create_vote/", views.create_panel_view, name="create_vote"),
    path("panel/<int:question_id>", views.panel_view, name="panel"),
]