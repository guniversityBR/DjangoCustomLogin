from django.db import models

from django.contrib.auth.models import AbstractUser, BaseUserManager


#Criando um gerenciador de usuario.

class UsuarioManager(BaseUserManager):

    user_in_migrations = True

    def _create_user(self, username, password, **extra_fields):
        if not username:
            raise ValueError('O Usuario é obrigatório')

        user = self.model(username=username, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user


#------------------------ Criando o Usuario Comum ----------------------------
    def create_user(self, username, password=None, **extra_fields):
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(username, password, **extra_fields)

#----------------------- Criando o super Usuario ----------------------------
    def create_superuser(self, username, password, **extra_fields):
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_staff', True)

        if extra_fields.get('is_superuser') is not True:
            raise ValueError('O super usuario precisa ter is_staff=True')

        if extra_fields.get('is_staff') is not True:
            raise ValueError('O super usuario precisar ter is_staff=True')

        return self._create_user(username, password, **extra_fields)

class CustomUsuario(AbstractUser):
    nome = models.CharField('Nome', max_length=100)
    username = models.CharField('Username', unique=True, max_length=20)
    email = models.EmailField('Email', unique=True)



    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'email']

    def __str__(self):
        return self.username

    objects = UsuarioManager()

