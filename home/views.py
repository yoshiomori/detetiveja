from django import http
from django.http import HttpResponse, FileResponse
from django.views import generic
import requests


class HomeView(generic.TemplateView):
    template_name = 'home/home.html'


class HomeV2View(generic.TemplateView):
    template_name = 'home/home.v2.html'


class GoogleView(generic.TemplateView):
    template_name = 'home/googlee7c3c15be2f23589.html'


class FaviconView(generic.View):
    @staticmethod
    def get(response):
        return http.FileResponse(
            streaming_content=open('home/templates/home/7295012_search_magnifier_find_zoom_glass_icon.ico', 'rb'),
            filename='favicon.ico',
            content_type='image/x-icon'
        )


class BingView(generic.TemplateView):
    template_name = 'home/BingSiteAuth.xml'
    content_type = 'application/xml'


class RobotsView(generic.TemplateView):
    template_name = 'home/robots.txt'
    content_type = 'text/plain'


class NextImageView(generic.View):
    @staticmethod
    def get(request):
        response = requests.get(request.GET.get('url'))
        return HttpResponse(response.content, content_type=response.headers['Content-Type'])


class NextStaticView(generic.View):
    @staticmethod
    def get(request, filename):
        with open(f'home/templates/home/{filename}') as fo:
            content = fo.read()
        return HttpResponse(content, content_type='text/css; charset=UTF-8')


class CFFontsView(generic.View):
    @staticmethod
    def get(request, filename):
        with open(f'home/templates/home/cf-fonts/{filename}') as fo:
            content = fo.read()
        return HttpResponse(content, headers=dict91)
