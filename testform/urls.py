from django.urls import path
from . import views


app_name = "testform"
urlpatterns = [
    path("form/", views.reg_form_view, name="reg_form"),
    path("list/", views.prop_lis_view, name = "prop_list"),
]