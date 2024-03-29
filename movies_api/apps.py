from django.apps import AppConfig


class MoviesApiConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "movies_api"
    
    def ready(self):
        # Import celery app now that Django is mostly ready.
        # This initializes Celery and autodiscovers tasks
        import movies_api.celery
