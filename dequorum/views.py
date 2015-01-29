from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required

from .forms import ThreadCreateForm
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


@login_required
def thread_create(request):

    if request.method == 'POST':
        form = ThreadCreateForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.owner = request.user
            obj.save()
            return redirect(obj)
    else:
        form = ThreadCreateForm()

    return render(request, 'dequorum/thread_create.html', {
        'form': form,
    })
