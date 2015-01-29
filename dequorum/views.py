from django.shortcuts import render

from .models import Thread


def thread_list(request):

    threads = Thread.objects.visible()

    return render(request, 'dequorum/thread_list.html', {
        'threads': threads,
    })
