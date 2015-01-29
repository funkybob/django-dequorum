
from django import forms

from . import models


class ThreadCreateForm(forms.ModelForm):

    class Meta:
        model = models.Thread
        fields = ['title',]
