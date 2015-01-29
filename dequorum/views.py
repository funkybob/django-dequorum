from django.shortcuts import render, get_object_or_404

from .models import Thread


def thread_list(request):

    threads = Thread.objects.visible()

    return render(request, 'dequorum/thread_list.html', {
        'threads': threads,
    })


def thread_detail(request, pk):
    thread = get_object_or_404(Thread.objects.visible(), pk=pk)

    return render(request, 'dequorum/thread_detail.html', {
        'thread': thread,
        'messages': thread.messages.visible(),
    })
