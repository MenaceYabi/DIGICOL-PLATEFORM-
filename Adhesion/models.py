from django.db import models


class Membre(models.Model):

    VILLES = [
        ("douala", "Douala"),
        ("yaounde", "Yaoundé"),
        ("autre", "Autre"),
    ]

    DOMAINES = [
        ("web", "Développement Web & Mobile"),
        ("data", "Data Science & Intelligence Artificielle"),
        ("networks", "Réseaux & Sécurité"),
        ("design", "Design UI/UX"),
    ]

    nom_complet = models.CharField(max_length=150)

    email = models.EmailField(
        unique=True
    )

    mot_de_passe = models.CharField(
        max_length=255
    )

    telephone = models.CharField(
        max_length=30
    )

    ville = models.CharField(
        max_length=30,
        choices=VILLES
    )

    domaine_interet = models.CharField(
        max_length=30,
        choices=DOMAINES
    )

    date_inscription = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return self.nom_complet

    class Meta:
        verbose_name = "Membre"
        verbose_name_plural = "Membres"
        ordering = ["-date_inscription"]