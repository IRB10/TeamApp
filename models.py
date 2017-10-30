# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals
from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=80)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()
    uloge_fk = models.ForeignKey("Uloge", models.DO_NOTHING)

    def __unicode__(self):
        return self.uloge_fk

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Destinacije(models.Model):
    destinacija_id = models.AutoField(primary_key=True)
    destinacija_naziv = models.CharField(max_length=50)
    destinacija_opis = models.TextField()
    korisnici_korisnik = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'destinacije'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Dnevnik(models.Model):
    dnevnik_id = models.AutoField(primary_key=True)
    dnevnik_korisnik = models.CharField(max_length=50, blank=True, null=True)
    dnevnik_akcija = models.CharField(max_length=200)
    dnevnik_vrijeme = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'dnevnik'


class Sportovi(models.Model):
    sport_id = models.AutoField(primary_key=True)
    sport_naziv = models.CharField(max_length=50)
    sport_opis = models.TextField(max_length=500)
    sport_tip = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'sportovi'


class Tereni(models.Model):
    teren_id = models.AutoField(primary_key=True)
    teren_naziv = models.CharField(max_length=200)
    teren_opis = models.TextField()
    slike_terena = models.FileField()
    destinacije_destinacija = models.ForeignKey(Destinacije, models.DO_NOTHING)

    def __unicode__(self):
        return str(self.destinacije_destinacija.destinacija_naziv)

    def __str__(self):
        return str(self.destinacije_destinacija.destinacija_naziv)

    class Meta:
        managed = False
        db_table = 'tereni'


class Termini(models.Model):
    termin_id = models.AutoField(primary_key=True)
    termin_opis = models.CharField(max_length=255, blank=True, null=True)
    broj_dolazaka = models.IntegerField()
    meksimalan_broj_dolazaka = models.IntegerField()
    termin_kreiran = models.DateTimeField(auto_now_add=True)
    vrijeme_termina = models.DateTimeField(auto_now=True)
    tereni_teren = models.ForeignKey(Tereni, models.DO_NOTHING)
    sportovi_sport = models.ForeignKey(Sportovi, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'termini'


class Uloge(models.Model):
    uloga_id = models.AutoField(primary_key=True)
    uloga_naziv = models.CharField(max_length=40)

    class Meta:
        managed = False
        db_table = 'uloge'
