from django.urls import path
from . import views

app_name = "the_app"
urlpatterns = [
    path("", views.welcome, name="welcome"),
    path("<int:item_id>/", views.item, name="item"),
    path("listings/", views.ItemListView.as_view(), name="listings"),
    path("filtered/", views.filtered_view, name="filtered"),
    path("new_item/", views.record_item, name="new_item"),
]
