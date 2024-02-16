from django.urls import path, re_path

from home.views import HomeView, GoogleView, FaviconView, BingView, RobotsView, HomeV2View, NextImageView, \
    NextStaticView, CFFontsView, ImageView

app_name = 'home'
urlpatterns = [
    path('googlee7c3c15be2f23589.html', GoogleView.as_view()),
    path('favicon.ico', FaviconView.as_view()),
    path('BingSiteAuth.xml', BingView.as_view()),
    path('robots.txt', RobotsView.as_view()),
    path('_next/image', NextImageView.as_view()),
    re_path('_next/static/(?P<filename>.+)', NextStaticView.as_view()),
    re_path('cf-fonts/(?P<filename>.+)', CFFontsView.as_view()),
    re_path('img/(?P<filename>.+)', ImageView.as_view()),
    path('v1', HomeView.as_view()),
    path('', HomeV2View.as_view()),
]
