from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

def index(request):
    return render(request, 'chatbot/index.html')

@csrf_exempt
def get_response(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        message = data.get('message', '').lower()
        
        response = "Je ne suis pas sûr de comprendre. Pouvez-vous reformuler ?"
        
        if 'bonjour' in message or 'salut' in message:
            response = "Bonjour ! Comment puis-je vous aider aujourd'hui ?"
        elif 'exercice' in message:
            response = "Vous pouvez trouver des exercices dans l'onglet 'Ressources'."
        elif 'connexion' in message or 'connecter' in message:
            response = "Vous pouvez vous connecter en cliquant sur 'Connexion' en haut à droite."
        elif 'inscription' in message or 'inscrire' in message:
            response = "L'inscription est gratuite pour les élèves et les enseignants."
        elif 'math' in message:
            response = "Nous avons beaucoup d'exercices de mathématiques. Allez voir dans les ressources !"
        
        return JsonResponse({'response': response})
    return JsonResponse({'error': 'Invalid request'}, status=400)
