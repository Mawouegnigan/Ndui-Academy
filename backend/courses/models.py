from django.db import models
from django.conf import settings


class DomaineEtude(models.Model):
    """
    Un domaine d'étude regroupe plusieurs parcours.
    Ex : "Étude biblique" est le premier domaine de Ndui Academy,
    mais d'autres domaines pourront être ajoutés plus tard sans refonte technique.
    """
    nom = models.CharField(max_length=150, unique=True)
    description = models.TextField(blank=True)
    date_creation = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nom


class Parcours(models.Model):
    """
    Un parcours regroupe plusieurs cours, au sein d'un domaine d'étude.
    """
    domaine = models.ForeignKey(
        DomaineEtude, on_delete=models.CASCADE, related_name="parcours"
    )
    nom = models.CharField(max_length=150)
    description = models.TextField(blank=True)
    duree_estimee_heures = models.PositiveIntegerField(default=0)
    prerequis = models.TextField(blank=True)
    date_creation = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.nom} ({self.domaine.nom})"


class Cours(models.Model):
    """
    Un cours regroupe des leçons, ressources et évaluations,
    au sein d'un parcours.
    """
    parcours = models.ForeignKey(
        Parcours, on_delete=models.CASCADE, related_name="cours"
    )
    titre = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    ordre = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["ordre"]

    def __str__(self):
        return self.titre


class Lecon(models.Model):
    """
    Une leçon est l'unité pédagogique la plus petite.
    La progression est séquentielle : une leçon se débloque
    après validation de la précédente (logique gérée côté vue/service).
    """
    cours = models.ForeignKey(
        Cours, on_delete=models.CASCADE, related_name="lecons"
    )
    titre = models.CharField(max_length=200)
    contenu = models.TextField()
    ordre = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["ordre"]

    def __str__(self):
        return self.titre