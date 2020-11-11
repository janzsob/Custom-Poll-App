from django.urls import path
from . import views

app_name = "poll_app"
urlpatterns = [
    path("", views.home_view, name="home"),
    path("create/", views.create_view, name="create"),
    path("vote/<int:poll_id>/", views.vote_view, name="vote"),
    path("result/<int:pk>/", views.ResultView.as_view(), name="result"),
    path("register/", views.register_view, name="register"),
    path("login/", views.login_view, name="login"),
    path("logout/", views.logout_view, name="logout"),
]
