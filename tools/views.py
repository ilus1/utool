from django.views import generic
from django.contrib import messages
from django.urls import reverse_lazy
from django.db import models
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse

from users.models import MyUserModel
from .filters import ToolFilter
from .models import Category, Tool, ToolDisposableParts, ToolWrench, ToolEletric
import re

class ToolDetailView(generic.DetailView):
    queryset = Tool.available.all()


class ToolListView(generic.ListView):
    category = None
    paginate_by = 9

    def get_queryset(self):
        queryset = ToolFilter(
            self.request.GET,
            queryset=Tool.objects.all()
        ).qs

        category_slug = self.kwargs.get("slug")
        if category_slug:
            self.category = get_object_or_404(Category, slug=category_slug)
            queryset = queryset.filter(category=self.category)

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["category"] = self.category
        context["categories"] = Category.objects.all()
        context["filter"] = ToolFilter(self.request.GET, queryset=self.get_queryset())
        return context


class NewToolView(generic.CreateView):

    def __init__(self, model=Tool):
        self.model = model
        self.base_category = Category.objects.get(name="Manuais")
        self.success_url = reverse_lazy("pages:list")
        self.template_name = "tools/new_tool.html"
        self.fields = ["name", "image", "description", "price",]
    
    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.category = self.base_category
        obj.owner = self.request.user
        obj.save()
        messages.success(self.request, "O Anúncio foi publicado com sucesso!")        
        return super(NewToolView, self).form_valid(form)


class NewToolDisposablePartsView(NewToolView):

    def __init__(self):
        super().__init__(ToolDisposableParts)
        self.base_category = Category.objects.get(name="Desgastáveis")
        self.fields.extend(["disposable_parts", "disposable_part_price"])


class NewToolWrenchView(NewToolView):
    
    def __init__(self):
        super().__init__(ToolWrench)
        self.base_category = Category.objects.get(name="Chaves")
        self.fields.pop(2)
        self.fields.extend(["size", "description"])


class NewToolEletricView(NewToolView):
    
    def __init__(self):
        super().__init__(ToolEletric)
        self.base_category = Category.objects.get(name="Elétricas")
        self.fields.extend(["voltage", "extra_part", "extra_part_specification"])


class DeleteToolView(generic.DeleteView):
    model = Tool
    success_url = reverse_lazy("pages:list")

    template_name = 'tools/delete_tool.html'

    def get(self, request, *args, **kwargs):
        
        self.object = self.get_object()
        
        if self.object.owner != self.request.user:
            return redirect(self.success_url)
        
        else:
            messages.success(self.request, "O Anúncio foi removido com sucesso!")    
            return render(request, self.template_name, {})



class ToolChoicesView(generic.TemplateView):
    template_name = "tools/tool_choices.html"
    redirect_url = reverse_lazy("pages:list")


    def get(self, request, *args, **kwargs):
        
        if request.user.adress == '':
            return redirect(self.redirect_url)
        
        else:
            return render(request, self.template_name, {})


class UserToolsListView(LoginRequiredMixin, ToolListView):
    template_name = 'tools/my_tools.html'

    def get_queryset(self):
        queryset = ToolFilter(
            self.request.GET,
            queryset=Tool.objects.filter(owner=self.request.user)
        ).qs

        category_slug = self.kwargs.get("slug")
        if category_slug:
            self.category = get_object_or_404(Category, slug=category_slug)
            queryset = queryset.filter(category=self.category)

        return queryset
