import json
from django.http import JsonResponse

def hello(request):
    data = { 'success': 'hello world'}
    return JsonResponse(json.dumps(data), safe=False)
