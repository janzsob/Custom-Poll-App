from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import PropForm
from .models import Property



def reg_form_view(request):
    if request.method == "POST":
        form = PropForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("testform:prop_list")
    else:
        form = PropForm()

    context = {"form": form}
    return render(request, "testform/reg_form.html", context)


def prop_lis_view(request):
    prop_list = Property.objects.all()
    context = {"prop_list": prop_list}
    return render(request, "testform/prop_list.html", context)