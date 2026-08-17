from django.shortcuts import render , redirect
from Adhesion.models import Membre
# Create your views here.
def MembreDASH(request):
    
    membre_id = request.session.get("membre_id")

    # Si le membre n'est pas connecté
    if not membre_id:
        return redirect("connexion")

    try:
        membre = Membre.objects.get(id=membre_id)

    except Membre.DoesNotExist:
        request.session.flush()
        return redirect("connexion")

    context = {
        "membre": membre
    }
    
    return render ( request  , 'Membre/membre.html' , context)