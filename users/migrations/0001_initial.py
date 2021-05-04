# Generated by Django 3.2 on 2021-05-04 03:10

import django.contrib.auth.models
import django.contrib.auth.validators
import django.core.validators
from django.db import migrations, models
import django.utils.timezone
import users.utils


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='MyUserModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('name', models.CharField(max_length=50, validators=[django.core.validators.RegexValidator(code='erro', message='Nome deve conter apenas letras e numeros.', regex='[0-9a-zA-Z]{3}[0-9a-zA-Z]*')], verbose_name='nome')),
                ('surname', models.CharField(max_length=700, validators=[django.core.validators.RegexValidator(code='erro', message='Sobrenome deve conter apenas letras, numeros e espacos.', regex='[0-9a-zA-Z ]{3}[0-9a-zA-Z ]*')], verbose_name='sobrenome')),
                ('cpf', models.CharField(help_text='Devera conter apenas numeros', max_length=11, unique=True, validators=[users.utils.validate_cpf])),
                ('adress', models.CharField(max_length=50, verbose_name='endereco')),
                ('number', models.CharField(max_length=5, validators=[django.core.validators.RegexValidator(code='erro', message='Deve conter apenas numeros maiores que 0', regex='[0-9]+')], verbose_name='numero')),
                ('complement', models.CharField(max_length=30, verbose_name='complemento')),
                ('district', models.CharField(max_length=30, verbose_name='bairro')),
                ('zip_code', models.CharField(max_length=8, verbose_name='cep')),
                ('city', models.CharField(max_length=30, verbose_name='cidade')),
                ('state', models.CharField(default='DF', max_length=2, verbose_name='estado')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]
