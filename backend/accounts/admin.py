from django.contrib import admin
from .models import Profil, Inscription


@admin.register(Profil)
class ProfilAdmin(admin.ModelAdmin):
    list_display = ("user", "role", "email_verifie", "date_creation")
    list_filter = ("role", "email_verifie")
    search_fields = ("user__username", "user__email")


@admin.register(Inscription)
class InscriptionAdmin(admin.ModelAdmin):
    list_display = ("profil", "parcours", "date_inscription")
    list_filter = ("parcours",)