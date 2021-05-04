from django.db import models
from .models import Tool
from django import forms
from users.models import MyUserModel


class NewTool(Tool):

    def __init__(self):
        super().__init__()

