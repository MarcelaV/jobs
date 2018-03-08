"""jobs URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""

from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import login, password_reset, password_reset_done, password_reset_confirm, password_reset_complete

import ofertas
from ofertas import views
from ofertas.views import HomeView, DetailView, CreateView, ListView, Postulacion
from users import views as users_views
from users.views import LoginView, LogoutView, RegistroUsuario





urlpatterns = [
    url(r'^admin/', admin.site.urls),

    #OFERTAS URLS
    url(r'^$', HomeView.as_view(), name='ofertas_home'),
    url(r'^ofertas/$', login_required(ListView.as_view()), name='ofertas_list'),
    url(r'^ofertas/(?P<pk>[0-9]+)$', login_required(DetailView.as_view()), name='ofertas_detail'),
    url(r'^ofertas/nueva$', login_required(CreateView.as_view()), name='crear_oferta'),


    #USERS URLS
    #url(r'^login$', LoginView.as_view(), name='users_login'),
    url(r'^accounts/login/$', login, {'template_name':'users/login.html'},  name='login'),
    url(r'^logout$', LogoutView.as_view(), name='users_logout'),

    #REGISTRO URLS
    url(r'^registrar$', RegistroUsuario.as_view(), name='registrar'),

    #POSTULAR URLS
    url(r'^ofertas/postular$', Postulacion.as_view(), name='postular'),

    #URLS RECUPERACION PASSWORD
    url(r'^reset/password_reset', password_reset, {'template_name': 'recuperacion/password_reset_form.html',
                                                   'email_template_name': 'recuperacion/password_reset_email.html'},
                                                    name='password_reset'),
    url(r'^password_reset_done', password_reset_done, {'template_name': 'recuperacion/password_reset_done.html'}, name='password_reset_done'),
    #url(r'^password_reset_done', password_reset_done, {'template_name': 'registration/password_reset_done.html'}, name='password_reset_done'),
    url(r'^reset/(?P<uidb64>[0-94-Za-z_\-]+)/(?P<token>.+)/$', password_reset_confirm, {'template_name': 'recuperacion/password_reset_confirm.html'}, name="password_reset_confirm"),
    url(r'^reset/done', password_reset_complete, {'template_name': 'recuperacion/password_reset_complete.html'}, name='password_reset_complete'),
]
