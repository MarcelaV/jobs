# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.shortcuts import render, redirect
from django.contrib.auth import logout as django_logout, authenticate, login as django_login
from django.views.generic import View
from users.forms import LoginForm


from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView
from django.core.urlresolvers import reverse_lazy


class LoginView(View):
    def get(self, request):
        error_messages = []
        form = LoginForm()
        context = {
            'errors': error_messages,
            'login_form': form
        }
        return render(request, 'users/login.html', context)



    def post(self, request):
        error_messages = []
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('usr')
            password = form.cleaned_data.get('pwd')
            user = authenticate(username=username, password=password)
            if user is None:
                error_messages.append('Nombre de usuario o password incorrecta')
            else:
                if user.is_active:
                    django_login(request, user)
                    url = request.GET.get('next', 'ofertas_home')
                    return redirect(url)
                else:
                    error_messages.append('El usuario no está activo')

        context = {
            'errors': error_messages,
            'login_form': form
        }
        return render(request, 'users/login.html', context)

class LogoutView(View):

    def get(self, request):
        if request.user.is_authenticated():
            django_logout(request)
        return redirect('ofertas_home')


class RegistroUsuario(CreateView):
    model = User
    template_name = 'users/registrar.html'
    form_class = LoginForm
    success_url = reverse_lazy('ofertas_home')

