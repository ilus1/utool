from .forms import UserChangeForm, UserCreationForm
from .models import MyUser
from django.views import generic
from django.urls import reverse_lazy

class ProfilePageView(generic.UpdateView):
    model = MyUser
    from_class = UserCreationForm
    template_name = 'account/profile.html'
    success_url = reverse_lazy('users:perfil')
    fields = ['nome', 'sobrenome', 'email', 'cpf', 'cep', 'endereco', 'numero', 'complemento', 'bairro', 'cidade', 'estado',]

    def get_object(self):
        return self.request.user