"""carrer_path_way URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.conf.urls import url

from carrerpath import views as c_path

from django.conf import settings

from django.conf.urls.static import static


urlpatterns = [
    url('admin/', admin.site.urls),

    url(r'^$', c_path.index, name='index'),

    url(r'^explore$', c_path.explore, name='explore'),

    url(r'^subscription$', c_path.subscription, name='subscription'),

    url(r'^resource$', c_path.resource, name='resource'),

    url(r'^article$', c_path.article, name='article'),

    url(r'^about$', c_path.about, name='about'),

    url(r'^contact$', c_path.contact, name='contact'),

    url(r'^signin$',c_path.signin,name='signin'),

    url(r'^signin1$',c_path.signin1,name='signin1'),

    url(r'^register$',c_path.register,name='register'),

    url(r'^register1$',c_path.register1,name='register1'),

    url(r'^StudentHome$',c_path.StudentHome,name='StudentHome'),

    url(r'^EmployeeHome$',c_path.EmployeeHome,name='EmployeeHome'),

    url(r'^vcounciler$',c_path.vcounciler,name='vcounciler'),

    url(r'^ViewDetails/(?P<id>\w+)',c_path.ViewDetails),

    url(r'^ChartDetails/(?P<eid>\w+)',c_path.ChartDetails),

    url(r'^ChartDetails1$',c_path.ChartDetails1),

    url(r'^vreplies$',c_path.vreplies,name='vreplies'),

    url(r'^vclients$',c_path.vclients,name='vclients'),

    


]
if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

