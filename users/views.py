from django.views import generic
from django.contrib import messages
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect

from .forms import UserChangeForm
from .models import MyUserModel

class ProfilePageView(generic.UpdateView):
    model = MyUserModel
    template_name = 'account/profile.html'
    success_url = reverse_lazy('users:profile')
    fields = ['name', 'surname', 'email', 'cpf', 'zip_code','adress', 'number', 'complement', 'district', 'city',]

    def form_valid(self, form):
        messages.success(self.request, 'Perfil atualizado com sucesso!')
        return HttpResponseRedirect(self.get_success_url())
    
    def get_object(self):
        return self.request.user



        