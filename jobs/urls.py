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
import ofertas
from ofertas import views
from ofertas.views import HomeView, DetailView, CreateView, ListView
from users import views as users_views
from users.views import LoginView, LogoutView

urlpatterns = [
    url(r'^admin/', admin.site.urls),

    #OFERTAS URLS
    url(r'^$', HomeView.as_view(), name='ofertas_home'),
    url(r'^ofertas/$', ListView.as_view(), name='ofertas_list'),
    url(r'^ofertas/(?P<pk>[0-9]+)$', DetailView.as_view(), name='ofertas_detail'),
    url(r'^ofertas/nueva$', CreateView.as_view(), name='crear_oferta'),


    #USERS URLS
    url(r'^login$', LoginView.as_view(), name='users_login'),
    url(r'^logout$', LogoutView.as_view(), name='users_logout'),

]
