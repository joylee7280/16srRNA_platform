"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from mainsite import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index),
    path('home/',views.home),
    path('login/',views.login),
    path('ancombc/',views.ancombc),
    path('lefse/',views.lefse), #新增一個網頁list只顯示所有的訊息
    path('ancom/',views.ancom),
    path('addproj/',views.addproj),
    path('manageproj/',views.manageproj),
    path('ancom/ancom-subject/',views.view_ancom),
    path('ancom/ancom/download_data/',views.download_data),
    path('ancom/ancom/download_ancom/',views.download_ancom),
    path('manageproj/download_ancomzip/',views.download_ancomzip),
    path('manageproj/download_ancombczip/',views.download_ancombczip),
    path('manageproj/download_lefsezip/',views.download_lefsezip),
    path('ancom/ancom/download_abun/',views.download_abun),
    path('ancombc/differentials_d/',views.view_ancombc_d),
    path('ancombc/differentials_b/',views.view_ancombc_b),
    path('ancombc/differentials_b/<str:item>',views.view_ancombc_barplot),
    path('lefse/lefse_output/',views.view_lefse_output),
    path('lefse/barplot/',views.view_lefse_b),
    path('lefse/cladogram/',views.view_lefse_c),
    path('image',views.image)

]
