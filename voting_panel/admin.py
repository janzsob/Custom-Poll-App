from django.contrib import admin
from .models import VoteQuestion, VoteChoice

admin.site.register(VoteQuestion)
admin.site.register(VoteChoice)
