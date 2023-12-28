"""BonePro URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import path, re_path
from .views import admin2, admin3, courses, themes, test, presentation, check, update, download, admin2, control_test, check_control, header, calculator, keep_alive

urlpatterns = [
    re_path(r'^/*$', courses, name='index'),
    path('themes/', courses),
    path('keep-alive/', keep_alive),
    path('themes/<int:id>', themes),
    path('calculator/', calculator),
    path('test/<int:id>/', test),
    path('control-test/<int:id>/', control_test),
    path('presentation/<int:id>/', presentation),
    path('check/<int:id>/', check),
    path('check-control/<int:id>/', check_control),
    path('update/', update),
    re_path(r'^admin2/(?P<slug>.*)/$', admin2),
    path('admin2/', admin3),
    path('download/', download),
    path('header/', header),
]
