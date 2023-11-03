from django.http import JsonResponse


# Create your views here.

def all_tasks(request):
    return JsonResponse({"message": "Hello, welcom to my task manager!"})
