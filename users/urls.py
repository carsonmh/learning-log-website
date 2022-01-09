from django.conf.urls import url
from django.contrib.auth.views import LoginView
from django.urls import path

from . import views

urlpatterns = [
    # log in page
    url('^login/$', LoginView.as_view(template_name='users/login.html'), name='login'),

    url('^logout/$', views.logout_view, name='logout'),

    url('^register/$', views.register, name='register'),
]



