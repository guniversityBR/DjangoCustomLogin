from django.views.generic.base import TemplateView
from django.contrib.auth.views import LoginView


class IndexView(TemplateView):
    template_name = 'index.html'


class CustomLoginView(LoginView):
    redirect_authenticated_user = '/admin/'
