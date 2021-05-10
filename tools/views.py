from django.views import generic
from django.contrib import messages
from django.urls import reverse_lazy
from django.db import models
from django.views.generic import DetailView, ListView, DeleteView
from django.shortcuts import get_object_or_404, render, redirect

from users.models import MyUserModel
from .filters import ToolFilter
from .models import Category, Tool, ToolDisposableParts, ToolWrench, ToolEletric
import re

class ToolDetailView(DetailView):
    queryset = Tool.available.all()


class ToolListView(ListView):
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

    def __init__(self, model=Tool, base_category=Category.objects.get(name="Manuais")):
        self.model = model
        self.base_category = base_category
        self.success_url = reverse_lazy("users:profile")
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
        super().__init__(ToolDisposableParts, Category.objects.get(name="Desgastáveis"))
        self.fields.extend(["disposable_parts", "disposable_part_price"])


class NewToolWrenchView(NewToolView):
    
    def __init__(self):
        super().__init__(ToolWrench, Category.objects.get(name="Chaves"))
        self.fields.pop(2)
        self.fields.extend(["size", "description"])


class NewToolEletricView(NewToolView):
    
    def __init__(self):
        super().__init__(ToolEletric, Category.objects.get(name="Elétricas"))
        self.fields.extend(["voltage", "extra_part", "extra_part_specification"])


class DeleteToolView(DeleteView):
    model = Tool
    success_url = reverse_lazy("pages:list")

    template_name = 'tools/delete_tool.html'

    def get(self, request, *args, **kwargs):
        
        self.object = self.get_object()
        
        if self.object.owner != self.request.user.email:
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
    