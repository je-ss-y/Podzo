from django.db import models
from .models import *
from django import forms
from django.contrib.auth.models import User




class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['comment']