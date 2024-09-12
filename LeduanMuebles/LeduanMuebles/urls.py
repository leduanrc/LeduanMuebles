"""
URL configuration for LeduanMuebles project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from LeduanMueblesApp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name="home"),

    path('platanitos', views.platanitos, name="platanitos"),
    path('brasilenos', views.brasilenos, name="brasilenos"),
    path('pelotas', views.pelotas, name="pelotas"),
    path('charlottes', views.charlottes, name="charlottes"),
    path('rottweilers', views.rottweilers, name="rottweilers"),
    path('panchos', views.panchos, name="panchos"),
    path('chesters', views.chesters, name="chesters"),
    path('comadritas', views.comadritas, name="comadritas"),
    path('sillones', views.sillones, name="sillones"),

    path('comedor4', views.comedor4, name="comedor4"),
    path('comedor6', views.comedor6, name="comedor6"),
    path('banquetas', views.banquetas, name="banquetas"),

    path('hierro', views.hierro, name="hierro"),
    path('madera', views.madera, name="madera"),
    path('capitoniada', views.capitoniada, name="capitoniada"),
    path('comoda', views.comoda, name="comoda"),
]

urlpatterns+=static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)