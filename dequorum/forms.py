
from django import forms
from django.forms import widgets

from . import models


class ThreadCreateForm(forms.ModelForm):

    class Meta:
        model = models.Thread
        fields = ['title']


class MessageCreateForm(forms.ModelForm):

    class Meta:
        model = models.Message
        fields = ['body']


class TagFilterForm(forms.Form):
    tag = forms.ModelMultipleChoiceField(
        queryset=models.Tag.objects.all(),
        required=True,
        widget=widgets.CheckboxSelectMultiple
    )