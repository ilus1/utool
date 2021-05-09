from django.views import generic
from django.contrib import messages
from django.urls import reverse_lazy
from django.views.generic import DetailView, ListView, DeleteView
from django.shortcuts import get_object_or_404, render, redirect

from users.models import MyUserModel
from .filters import ToolFilter
from .models import Category, Tool, ToolDisposableParts, ToolWrench, ToolEletric


class ToolDetailView(DetailView):
    queryset = Tool.available.all()


class ToolListView(ListView):
    category = None
    paginate_by = 6

    def get_queryset(self):
        queryset = Tool.available.all()

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

class ToolChoicesView(generic.TemplateView):
    template_name = "tools/tool_choices.html"


class NewToolView(generic.CreateView):
    
    def __init__(self, model=Tool):
        self.model = model
        self.success_url = reverse_lazy("users:profile")
        self.template_name = "tools/new_tool.html"
        self.fields = ["category","name", "image", "description", "price",]
    
    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.owner = self.request.user.email
        obj.save()
        messages.success(self.request, "O Anúncio foi publicado com sucesso!")        
        return super(NewToolView, self).form_valid(form)


class NewToolDisposablePartsView(NewToolView):
    
    def __init__(self):
        super().__init__(ToolDisposableParts)
        self.fields.extend(["disposable_parts", "disposable_part_price"])


class NewToolWrenchView(NewToolView):
    
    def __init__(self):
        super().__init__(ToolWrench)
        self.fields.extend(["size"])


class NewToolEletricView(NewToolView):
    
    def __init__(self):
        super().__init__(ToolEletric)
        self.fields.extend(["voltage", "extra_part", "extra_part_specification"])


class DeleteToolView(DeleteView):
    model = Tool
    success_url = reverse_lazy("users:profile")
    error_url = reverse_lazy("pages:list")

    template_name = 'tools/delete_tool.html'

    def get(self, request, *args, **kwargs):
        
        self.object = self.get_object()
        
        if self.object.owner != self.request.user.email:
            return redirect(self.error_url)
        
        else:
            return render(request, self.template_name, {})