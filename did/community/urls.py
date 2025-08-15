from django.urls import path
from django.http import JsonResponse


def placeholder(request):
    return JsonResponse({"message": "Analytics API coming soon"})

urlpatterns = [
    path('', placeholder),
    
]
