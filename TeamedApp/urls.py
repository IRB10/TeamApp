from django.conf.urls import url
from . import views
from django.contrib.auth.views import (
    password_reset,
    password_reset_done,
    password_reset_confirm,
    password_reset_complete
)
from TeamedApp import views as core_views

urlpatterns = [
    url(r'^start$', views.start, name='start'),
    url(r'^home', views.home, name='home'),
    url(r'^registracija', views.registration, name='registration'),
    #url(r'^sportovi', views.sport, name='sport'),
    #url(r'^dodjela_uloge', views.dodjelauloge, name='dodjelauloge'),
    url(r'^tereni$', views.teren, name='teren'),
    url(r'^create$', views.create),
    url(r'^termini', views.termini, name='termin'),
    #url(r'^destinacije', views.destinacije, name='destinacija'),
    url(r'^prikazdestinacija$', views.prikazidestinacije, name='prikazidestinaciju'),
    url(r'^prikazdestinacije', views.prikazdestinacija, name='prikazidestinacij'),
    url(r'^prikazterena', views.prikaziterene, name='prikaziterene'),
    url(r'^prikazdestinacijaa$', views.prikaziteren, name='prikaziteren'),
    url(r'^prikaztermina$', views.prikazitermine, name='prikazitermin'),
    url(r'^prikazterminaa$', views.prikaziterminenakondolaska, name='termindolazak'),
    url(r'^dodjela_uloge/$', views.dodjelauloge, name='duloge'),
    url(r'^uredi$', views.uredi, name='uredi'),
    url(r'^password', views.change_password, name='promjeni_lozinku'),
    url(r'^ponovno_postavljanje_lozinke/$', password_reset, {'template_name': 'reset_password.html',
                                               'post_reset_redirect': 'password_reset_done',
                                               'email_template_name': 'reset_password_email.html'},
        name='reset_password'),
    url(r'^ponovno_postavljanje_lozinke/gotovo/$', password_reset_done, {'template_name': 'reset_password_done.html'},
        name='password_reset_done'),

    url(r'^ponovno_postavljanje_lozinke/potvrda/(?P<uidb64>[0-9A-Za-z]+)-(?P<token>.+)/$',
        password_reset_confirm, {'template_name': 'reset_password_confirm.html',
                                 'post_reset_redirect': 'password_reset_complete'},
        name='password_reset_confirm'),

    url(r'^ponovno_postavljanje_lozinke/zavrseno/$', password_reset_complete,
        {'template_name': 'reset_password_complete.html'}, name='password_reset_complete'),
    url(r'^profil', views.pregledaj_profil, name='profil'),
    url(r'^profil/(?P<pk>\d+)/$', views.pregledaj_profil, name='profil_s_pk'),
    url(r'^o_nama', views.onama, name='o_nama'),
]