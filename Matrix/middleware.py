from django.shortcuts import render
from django.conf import settings

class CustomErrorMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        if response.status_code == 400:
            return render(request, '400.html', status=400)
        elif response.status_code == 403:
            return render(request, '403.html', status=403)
        elif response.status_code == 404:
            return render(request, '404.html', status=404)
        elif response.status_code == 500:
            return render(request, '500.html', status=500)
        return response
