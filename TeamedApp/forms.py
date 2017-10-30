from datetime import datetime
from django.contrib.auth.forms import AuthenticationForm
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from TeamedApp.models import Sportovi, AuthUser, Uloge, Tereni, Destinacije, Termini

# If you don't do this you cannot use Bootstrap CSS
ROLES = (
    ('1', 'Administrator'),
    ('2', 'Moderator'),
    ('3', 'Registrirani korisnik'),
    ('4', 'Neregistrirani korisnik'),
)
VRSTA_SPORTA = (
    ('1', 'Individualni'),
    ('2', 'Timski'),
)


class EditProfileForm(UserChangeForm):

    class Meta:
        model = User
        fields = (
            'email',
            'first_name',
            'last_name',
            'password'
        )


class RegistrationForm(UserCreationForm):

    email = forms.EmailField(max_length=254, help_text='Unesite email.')

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', )


def kor_ime_dohvati():
    return AuthUser.objects.values('username')


def unique_valuesuloge():
    return Uloge.objects.values_list('uloga_id', 'uloga_naziv').distinct()


class DestinacijeForm(forms.ModelForm):
    class Meta:
        model = Destinacije
        fields = ('destinacija_naziv', 'destinacija_opis', 'korisnici_korisnik',)


class TerminiForm(forms.ModelForm):
    vrijeme_termina = forms.DateTimeField(initial=datetime.now(), required=False)
    class Meta:
        model = Termini
        fields = ('termin_opis', 'broj_dolazaka', 'meksimalan_broj_dolazaka', 'vrijeme_termina', 'tereni_teren', 'sportovi_sport')


class TereniForm(forms.ModelForm):
    class Meta:
        model = Tereni
        fields = ('teren_naziv', 'teren_opis','slike_terena')


class UserForm(forms.ModelForm):
    username = forms.CharField(widget=forms.Select(
        choices=AuthUser.objects.all().values_list('id', 'username')
        )
     )

    class Meta:
        model = AuthUser
        fields = ('username', 'uloge_fk',)


class SportoviForm(forms.ModelForm):
    sport_naziv = forms.CharField(label="Naziv", max_length=50)
    sport_opis = forms.Textarea(attrs={'cols': 100, 'rows': 50})
    sport_tip = forms.CharField(widget=forms.Select(
        choices=VRSTA_SPORTA
        )
     )

    class Meta:
        model = Sportovi
        fields = ('sport_naziv', 'sport_opis', 'sport_tip')


class LoginForm(AuthenticationForm):
    username = forms.CharField(label="Korisnicko ime", max_length=30,
                               widget=forms.TextInput(attrs={'class': 'form-control', 'name': 'korime'}))
    password = forms.CharField(label="Lozinka", widget=forms.PasswordInput(attrs={'class': 'form-control', 'name': 'lozinka'}))