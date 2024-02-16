import os

from django import http
from django.http import HttpResponse, FileResponse, HttpResponseRedirect, HttpResponsePermanentRedirect
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


class ImageView(generic.View):
    @staticmethod
    def get(response, filename):
        return http.FileResponse(
            streaming_content=open(f'home/templates/home/img/{filename}', 'rb'),
            filename=filename
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
        return HttpResponseRedirect(request.GET.get('url'))


class NextStaticView(generic.View):
    @staticmethod
    def get(request, filename):
        sfn = f'home/templates/home/{filename}'
        if not os.path.exists(sfn):
            response = requests.get(f'https://detetiveja.mydurable.com/_next/static/{filename}')
            assert response.ok
            with open(sfn, 'wb') as file_object:
                file_object.write(response.content)
        with open(sfn, encoding='utf-8') as file_object:
            content = file_object.read()

        _, ext = os.path.splitext(filename)
        if ext == '.js':
            content_type = 'text/javascript'
        elif ext == '.css':
            content_type = 'text/css'
        else:
            content_type = 'text/plain'

        return HttpResponse(content, content_type=content_type)


class CFFontsView(generic.View):
    @staticmethod
    def get(request, filename):
        with open(f'home/templates/home/cf-fonts/{filename}', 'rb') as file_object:
            content = file_object.read()
        headers = dict()
        headers['Content-Disposition'] = f'attachment; filename={os.path.basename(filename)}'
        return HttpResponse(
            content,
            headers=headers,
            content_type='font/woff2'
        )
