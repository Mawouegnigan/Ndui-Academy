from django.contrib import admin
from .models import DomaineEtude, Parcours, Cours, Lecon


@admin.register(DomaineEtude)
class DomaineEtudeAdmin(admin.ModelAdmin):
    list_display = ("nom", "date_creation")
    search_fields = ("nom",)


@admin.register(Parcours)
class ParcoursAdmin(admin.ModelAdmin):
    list_display = ("nom", "domaine", "duree_estimee_heures")
    list_filter = ("domaine",)
    search_fields = ("nom",)


@admin.register(Cours)
class CoursAdmin(admin.ModelAdmin):
    list_display = ("titre", "parcours", "ordre")
    list_filter = ("parcours",)


@admin.register(Lecon)
class LeconAdmin(admin.ModelAdmin):
    list_display = ("titre", "cours", "ordre")
    list_filter = ("cours",)