# -*- coding: utf-8 -*-
from __future__ import print_function
from __future__ import print_function
from __future__ import unicode_literals
from models import AuthUser, Uloge, Tereni, Destinacije, Termini, KorisnikTermin
from TeamedApp.forms import (
    RegistrationForm,
    EditProfileForm,
    DestinacijeForm,
    SportoviForm,
    UserForm,
    TereniForm,
    TerminiForm
)

from django.shortcuts import render, redirect
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.decorators import login_required
#from datetime import datetime
import datetime
from django.db.models import Q

# Create your views here.


def onama(request):
    return render(request, "o_nama.html")


@login_required(login_url="login/")
def home(request):
    return render(request, "home.html")


def start(request):
    korisnici = AuthUser.objects.all()
    contex = {'user': korisnici}
    return render(request, "base.html", contex)

@login_required(login_url="login/")
def prikazdestinacija(request):
    kk = request.user
    pk = kk.id
    korisnik = AuthUser.objects.get(pk=pk)
    dest1 = Destinacije.objects.filter(korisnici_korisnik_id=pk)
    return render(request, 'destinacijezamoderatore.html', {'dest1': dest1, 'korisnik': korisnik})


def prikazidestinacije(request):
    dest = Destinacije.objects.all()

    return render(request, "prikazidestinacije.html", {"dest": dest})


@login_required(login_url="login/")
def pregledaj_profil(request):
    kk = request.user
    pk = kk.id
    korisnik = AuthUser.objects.get(pk=pk)
    if pk:
        user = AuthUser.objects.get(pk=pk)
    else:
        user = request.user
    args = {'user': user}
    return render(request, 'profil.html', args, korisnik)


def prikaziterene(request):
    ter = Tereni.objects.all()
    return render(request, "terenizadestinacije.html", {"ter": ter})


def prikazitermine(request):
    terminmoj = request.GET.get('ter', '')
    kor = request.GET.get('kor', '')
    danas = datetime.datetime.today()
    varijabla = ""
    dajtermin = Termini.objects.filter(tereni_teren_id=terminmoj, vrijeme_termina__gte=danas)
    return render(request, 'terminizaterene.html', {"dajtermin": dajtermin, 'varijabla': varijabla})


@login_required(login_url="login/")
def prikaziterminenakondolaska(request):
    terminmoj = request.GET.get('terentermin', '')
    korisniktermin = request.GET.get('terminkorisnik', '')
    terminid = request.GET.get('termin', '')
    danas = datetime.datetime.today()
    korisnik = AuthUser.objects.get(pk=korisniktermin)
    dobijTermin = Termini.objects.get(termin_id=terminid)
    brojdolazaka = dobijTermin.broj_dolazaka
    maxbrojdolazaka = dobijTermin.meksimalan_broj_dolazaka
    vrijeme = dobijTermin.vrijeme_termina
    if brojdolazaka == maxbrojdolazaka:
        brojdolazaka = dobijTermin.broj_dolazaka
        varijabla = "Žao nam je maksimalan broj dolazaka je prijavljen!"
    else:
        brojdolazaka += 1
        dajKorisnika = KorisnikTermin.objects.filter(id_korisnik_id=korisniktermin, id_termin_id=terminid).first()
        if dajKorisnika is None:
            varijabla = "Uspješno ste prijavili termin "
            spremizapis = KorisnikTermin(id_korisnik=korisnik, id_termin=dobijTermin)
            dodajDolazak = Termini(termin_id=terminid, broj_dolazaka=brojdolazaka, vrijeme_termina=vrijeme)
            dodajDolazak.save(update_fields=["broj_dolazaka", "vrijeme_termina"])
            spremizapis.save()
        else:
            varijabla = "Već ste prijavljeni na ovaj termin "
    dajtermin = Termini.objects.filter(tereni_teren_id=terminmoj, vrijeme_termina__gte=danas)
    return render(request, 'terminizaterene.html', {"dajtermin": dajtermin, 'korisnik': korisnik, "varijabla": varijabla})


def prikaziteren(request):
    te = request.GET.get('d', '')
    k = Tereni.objects.filter(destinacije_destinacija_id=te)
    #k = Tereni.objects.values('teren_naziv','teren_opis', 'slike_terena').filter(destinacije_destinacija_id=te)
    return render(request, "terenipodestinacijama.html", {"k": k})


@login_required(login_url="login/")
def create(request):
    korisnici = AuthUser.objects.all()
    uloga = Uloge.objects.get(pk=request.POST['uloge_fk'])
    korisnik = AuthUser(username=request.POST['username'], password=request.POST['password'], first_name=request.POST.get('name'), last_name=request.POST.get('prezime'), email=request.POST['email'], uloge_fk=uloga)
    korisnik.save()
    return redirect('/')


@login_required(login_url="login/")
def teren(request):
    kk = request.user
    pk = kk.id
    korisnik = AuthUser.objects.get(pk=pk)
    dest = Destinacije.objects.filter(korisnici_korisnik_id=pk)
    if korisnik.uloge_fk_id == 2 or korisnik.uloge_fk_id == 1:
        if request.method == 'POST':
            form = TereniForm(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                return redirect('home')
        else:
            form = TereniForm()
        return render(request, 'dodaj_teren.html', {'form': form, 'dest': dest, 'korisnik': korisnik})
    else:
        return render(request, 'home.html')


@login_required(login_url="login/")
def destinacije(request):
    if request.method == 'POST':
        form = DestinacijeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = DestinacijeForm()
    return render(request, 'destinacije.html', {'form': form})


@login_required(login_url="login/")
def termini(request):
    kk = request.user
    pk = kk.id
    korisnik = AuthUser.objects.get(pk=pk)
    if korisnik.uloge_fk_id == 2 or korisnik.uloge_fk_id == 1 or korisnik.uloge_fk_id == 3:
        if request.method == 'POST':
            form = TerminiForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('home')
        else:
            form = TerminiForm()
        return render(request, 'termin.html', {'form': form, 'korisnik': korisnik})
    else:
        return redirect('home')

@login_required(login_url="login/")
def sport(request):
    kk = request.user
    pk = kk.id
    korisnik = AuthUser.objects.get(pk=pk)
    if request.method == 'POST':
        form = SportoviForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = SportoviForm()
    return render(request, 'sport.html', {'form': form, 'korisnik': korisnik})


@login_required(login_url="login/")
def dodjelauloge(request):
    kk = request.user
    pk = kk.id
    korisnik = AuthUser.objects.get(pk=pk)
    uloga_id = korisnik.uloge_fk_id
    if uloga_id == 1:
        if request.method == 'POST':
            form = UserForm(request.POST)
            if form.is_valid():
                uloga = Uloge.objects.get(pk=request.POST['uloge_fk'])
                korisnik = AuthUser(id=request.POST['username'], uloge_fk=uloga)
                korisnik.save(update_fields=["uloge_fk"])
                return redirect('home')
        else:
            form = UserForm()
        return render(request, 'kreiraj_korisnika.html', {'form': form, 'korisnik': korisnik})
    else:
        return redirect('home')

@login_required(login_url="login/")
def uredi(request):
    kk = request.user
    pk = kk.id
    korisnik = AuthUser.objects.get(pk=pk)
    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance=request.user)

        if form.is_valid():
            form.save()
            return redirect('profil')
    else:
        form = EditProfileForm(instance=request.user)
        args = {'form': form}
        return render(request, 'promjeni_podatke.html', args, korisnik)


@login_required(login_url="login/")
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(data=request.POST, user=request.user)

        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return redirect('profil')
        else:
            return redirect('promjena_lozinke')
    else:
        form = PasswordChangeForm(user=request.user)

        args = {'form': form}
        return render(request, 'promjena_lozinke.html', args)


def registration(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            #username = form.cleaned_data.get('username')
            #raw_password = form.cleaned_data.get('password1')
            #user = authenticate(username=username, password=raw_password)
            #login(request, user)
            return redirect('login')
    else:
        form = RegistrationForm()
    return render(request, 'registration.html', {'form': form})

