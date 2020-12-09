from django.shortcuts import render, get_object_or_404, get_list_or_404, redirect
from django.http import HttpResponse, Http404
from .models import Listings
import datetime
from .forms import NewItemForm
from django.views import generic



def welcome(request):
    return HttpResponse("Let's reboot coding skills!")


# view for get the certain item
def item(request, item_id):
    req_item = get_object_or_404(Listings, pk=item_id)
    return render(request, "the_app/detail.html", {"req_item": req_item})


"""
# List of items ordered by date. 
def item_list(request):
    latest_items = Listings.objects.order_by("-list_date")
    context = {"latest_items": latest_items}
    return render(request, "the_app/listings.html", context)
"""
# List of items
class ItemListView(generic.ListView):
    template_name = "the_app/listings.html"
    context_object_name = "latest_items"

    def get_queryset(self):
        return Listings.objects.order_by("-list_date")


def filtered_view(request):
    #filtered_objects = get_list_or_404(Listings, condition="NEW")
    start_date = datetime.date(2020, 9, 28)
    end_date = datetime.date(2020, 9, 30)
    filtered_objects = get_list_or_404(Listings, list_date__range=(start_date, end_date))
    context = {"filtered_objects": filtered_objects}
    return render(request, "the_app/filtered.html", context)


"""View for record new item
def record_item(request):
    if request.method != "POST":
        form = NewItemForm()
    else:
        form = NewItemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("the_app:listings")
    
    context = {"form": form}
    return render(request, "the_app/new_item.html", context)
"""    

# view for record new item in form
def record_item(request):
    if request.method == "POST":
        form = NewItemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("the_app:listings")
    else:
        form = NewItemForm()
    
    context = {"form": form}
    return render(request, "the_app/new_item.html", context)
