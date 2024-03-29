
from django.contrib import admin
from django.apps import apps

movie_models = apps.get_app_config("movies_api").get_models()
for model in movie_models:
    try:
        admin.site.register(model)
    except admin.sites.AlreadyRegistered:
        pass