from math import ceil
from django.shortcuts import render, redirect
from django.core.paginator import Paginator, EmptyPage

from . import models

# Create your views here.
def all_rooms(request):
    page = request.GET.get("page", 1)
    room_list = models.Room.objects.all()
    paginator = Paginator(room_list, 10, orphans=2)
    try:
        rooms_page = paginator.page(int(page))
        return render(request, "rooms/home.html", {"pages": rooms_page})
    except EmptyPage:
        return redirect("/")
