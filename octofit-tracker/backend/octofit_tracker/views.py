from django.http import JsonResponse
import os

def api_root(request):
    codespace_url = "https://jubilant-winner-6994q75jr5q9fr776-8000.app.github.dev"
    localhost_url = "http://localhost:8000"
    
    # Return both URLs for testing purposes
    return JsonResponse({
        "codespace_url": codespace_url,
        "localhost_url": localhost_url
    })
