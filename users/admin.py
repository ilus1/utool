from django.contrib import admin
from django.contrib.auth import admin as auth_admin
from .forms import UserChangeForm, UserCreationForm
from .models import MyUserModel


@admin.register(MyUserModel)

class UserAdmin(auth_admin.UserAdmin):
    form = UserChangeForm
    add_form = UserCreationForm
    model = MyUserModel
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        (('Personal info'), {'fields': ('name', 'surname', 'email', 'cpf', 'zip_code', 'adress', 'number', 'complement', 'district', 'city', 'state',)}),
        (('Permissions'), {
            'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions'),
        }),
        (('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )
