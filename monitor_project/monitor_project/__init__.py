default_app_config = "monitor_app.apps.MonitorAppConfig"

from .celery import app as celery_app

__all__ = ("celery_app",)
