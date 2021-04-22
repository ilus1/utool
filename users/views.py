from .forms import UserChangeForm
from .models import MyUser
from django.views import generic
from django.urls import reverse_lazy

class ProfilePageView(generic.UpdateView):
    model = MyUser
    from_class = UserChangeForm
    template_name = 'account/profile.html'
    success_url = reverse_lazy('users:profile')
    fields = ['name', 'surname', 'email', 'cpf', 'zip_code', 'adress', 'number', 'complement', 'district', 'city', 'state',]

    def get_object(self):
        return self.request.user