from typing import Optional

from django.apps import AppConfig
from django.db.models import TextField, Q
from django.forms import Field


class MainConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'main'
    #
    # def ready(self):
    #     from django.contrib import admin
    #     from django.contrib.admin import sites
    #
    #     class MyAdminSite(AdminSiteSearchView, admin.AdminSite):
    #         def filter_field(self, query: str, field: Field) -> Optional[Q]:
    #             """Extends super() to add TextField support to site search"""
    #             if isinstance(field, TextField):
    #                 return Q(**{f"{field.name}__icontains": query})
    #             return super().filter_field(query, field)
    #
    #     mysite = MyAdminSite()
    #     admin.site = mysite
    #     sites.site = mysite
