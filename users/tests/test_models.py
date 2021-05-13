import pytest

from ..models import MyUserModel

pytestmark = pytest.mark.django_db

def test_create_user():
    user = MyUserModel.objects.create_user(
        name="usuario_test", surname="sobrenome",email="usuario@test.com", 
        password="passw0rd", cpf="03595068106", username="username"
    )

    assert user.username == "username"
    assert user.name == "usuario_test"
    assert user.surname == "sobrenome"
    assert user.cpf == "03595068106"
    assert user.email == "usuario@test.com"
    assert user.is_active
    assert not user.is_staff
    assert not user.is_superuser

def test_create_superuser():
    user = MyUserModel.objects.create_superuser(
        username="admin_test", password="passw0rd"
    )
    assert user.username == "admin_test"
    assert user.is_active
    assert user.is_staff
    assert user.is_superuser