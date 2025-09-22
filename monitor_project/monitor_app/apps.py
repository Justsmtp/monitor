from django.apps import AppConfig

class MonitorAppConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "monitor_app"

    def ready(self):
        # Import inside ready() to avoid early execution
        from .tasks import start_monitor
        start_monitor()
