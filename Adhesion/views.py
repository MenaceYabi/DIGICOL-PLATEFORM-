from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.hashers import make_password, check_password

from .models import Membre


def Adhesion(request):

    if request.method == "POST":

        nom_complet = request.POST.get("fullname", "").strip()
        email = request.POST.get("email", "").strip().lower()
        mot_de_passe = request.POST.get("password", "")
        confirmation = request.POST.get("confirm_password", "")
        telephone = request.POST.get("phone", "").strip()
        ville = request.POST.get("city", "")
        domaine = request.POST.get("domain", "")

        # Vérification des champs obligatoires
        if not nom_complet or not email or not mot_de_passe:
            messages.error(
                request,
                "Veuillez remplir tous les champs obligatoires."
            )
            return render(
                request,
                "Adhesion/adhesion.html"
            )

        # Vérification des mots de passe
        if mot_de_passe != confirmation:
            messages.error(
                request,
                "Les mots de passe ne correspondent pas."
            )
            return render(
                request,
                "Adhesion/adhesion.html"
            )

        # Vérification de l'email
        if Membre.objects.filter(email=email).exists():
            messages.error(
                request,
                "Cette adresse email est déjà utilisée."
            )
            return render(
                request,
                "Adhesion/adhesion.html"
            )

        # Création du membre
        membre = Membre.objects.create(
            nom_complet=nom_complet,
            email=email,
            mot_de_passe=make_password(mot_de_passe),
            telephone=telephone,
            ville=ville,
            domaine_interet=domaine
        )

        messages.success(
            request,
            "Votre compte DigiCol a été créé avec succès. Connectez-vous pour accéder à votre espace."
        )

        return redirect("connexion")


    return render(
        request,
        "Adhesion/adhesion.html"
    )


def connexion(request):

    if request.method == "POST":

        email = request.POST.get("email", "").strip().lower()
        mot_de_passe = request.POST.get("password", "")

        try:
            membre = Membre.objects.get(email=email)

        except Membre.DoesNotExist:

            messages.error(
                request,
                "Email ou mot de passe incorrect."
            )

            return render(
                request,
                "Adhesion/connexion.html"
            )

        # Vérification du mot de passe
        if check_password(
            mot_de_passe,
            membre.mot_de_passe
        ):

            # Création de la session
            request.session["membre_id"] = membre.id
            request.session["membre_nom"] = membre.nom_complet
            request.session["membre_email"] = membre.email

            messages.success(
                request,
                f"Bienvenue {membre.nom_complet} !"
            )

            return redirect("Membre")

        messages.error(
            request,
            "Email ou mot de passe incorrect."
        )

    return render(
        request,
        "Adhesion/connexion.html"
    )


def deconnexion(request):

    request.session.flush()

    messages.success(
        request,
        "Vous avez été déconnecté avec succès."
    )

    return redirect("connexion")