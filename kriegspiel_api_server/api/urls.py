# -*- coding: utf-8 -*-
from django.conf.urls import url
from api import views

urlpatterns = (
    url(r'^auth/sign_in/?$', views.SignInView.as_view(), name='api_sign_in'),
    url(r'^game/?$', views.GamesView.as_view(), name='api_game'),
)