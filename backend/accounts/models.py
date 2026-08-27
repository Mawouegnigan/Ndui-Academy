from django.db import models
from django.contrib.auth.models import User


class Profil(models.Model):
    """
    Étend le modèle User par défaut de Django avec les informations
    spécifiques à un apprenant (ou administrateur) de Ndui Academy.
    Relation one-to-one : chaque compte utilisateur a un seul profil.
    """
    ROLE_CHOICES = [
        ("apprenant", "Apprenant"),
        ("admin", "Administrateur"),
        ("mentor", "Mentor"),
    ]

    user = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name="profil"
    )
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default="apprenant")
    date_naissance = models.DateField(null=True, blank=True)
    photo = models.ImageField(upload_to="profils/", null=True, blank=True)
    email_verifie = models.BooleanField(default=False)
    date_creation = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} ({self.role})"


class Inscription(models.Model):
    """
    Trace l'inscription d'un apprenant à un parcours donné.
    Un apprenant peut s'inscrire à plusieurs parcours (relation many-to-many
    matérialisée explicitement pour pouvoir suivre la date et la progression).
    """
    profil = models.ForeignKey(
        Profil, on_delete=models.CASCADE, related_name="inscriptions"
    )
    parcours = models.ForeignKey(
        "courses.Parcours", on_delete=models.CASCADE, related_name="inscriptions"
    )
    date_inscription = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ("profil", "parcours")

    def __str__(self):
        return f"{self.profil.user.username} -> {self.parcours.nom}"