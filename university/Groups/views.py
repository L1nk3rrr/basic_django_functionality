from django.shortcuts import render

from .models import Group


def group_list(request):
    group = Group.objects.all()
    return render(request, 'group_list.html', {'groups': group})
