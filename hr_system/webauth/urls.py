from django.urls import path
from django.conf.urls import url
from webauth.views import activate, signup
from django.views.generic import TemplateView

app_name = 'webauth'

urlpatterns = [
    path('signup/', signup, name='signup'),
    path('signup/signup_complete/', TemplateView.as_view(template_name="registration/signup_complete.html"),
         name='signup_complete'),
    url(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,40})/$',
        activate, name='activate'),
]