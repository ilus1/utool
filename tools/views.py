from django.shortcuts import get_object_or_404
from django.views.generic import DetailView, ListView
from django.views import generic
from django.urls import reverse_lazy
from django.contrib import messages

from .models import Category, Tool
from users.models import MyUserModel
from .forms import NewTool

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
        return context


class NewToolView(generic.CreateView):
    model = NewTool
    template_name = 'tools/new_tool.html'
    success_url = reverse_lazy('users:profile')
    fields = ['category','name', 'image', 'description', 'price', 'is_available',]
    
    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.owner = self.request.user.email
        obj.save()
        messages.success(self.request, 'O Anúncio foi publicado com sucesso!')        
        return super(NewToolView, self).form_valid(form)
