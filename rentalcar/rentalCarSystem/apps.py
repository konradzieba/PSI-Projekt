from django.apps import AppConfig


class RentalcarsystemConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'rentalCarSystem'

    def ready(self):
        from . import singals