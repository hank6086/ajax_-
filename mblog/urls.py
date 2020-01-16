"""mblog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path, include
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
from django.conf.urls.static import static
# import sys
# sys.path.append("..")
# sys.path.append("mainsite")
from mainsite.views import homepage, test, id_naid,megwindows,add

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', homepage),
    path('test/', test),
    path('id_ap/', id_naid),
    path('meg/',megwindows),
    path('add/',add)
    # path('regist/', regist),
    # path('login/', login),
    # path('logout', logout)
    # path('set_s',set_session),
    # path('get_s',get_session),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
