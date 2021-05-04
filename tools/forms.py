from django.db import models
from .models import Tool
from django import forms
from users.models import MyUserModel


class NewTool(Tool):

    def __init__(self, *args):
        super().__init__()
        
""" class NewTool_ScrewDriver(Tool):
    size = 

    def __init__(self, *args):
        super().__init__()
         """
