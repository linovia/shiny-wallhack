from django.conf.urls import patterns, url
from django.views.generic import TemplateView
from . import views


urlpatterns = patterns('',
    url(r'^$',
        TemplateView.as_view(template_name='home.html'),
        name='homepage'),

    url(r'^signup/$',
        views.SignupView.as_view(),
        name='signup'),

    url(r'^welcome/$',
        TemplateView.as_view(template_name='welcome.html'),
        name='welcome'),
)
