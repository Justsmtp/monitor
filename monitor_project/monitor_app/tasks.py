import time
import threading
from django.contrib.auth import get_user_model
from celery import shared_task


def monitor_users_loop():
    """
    Loop that monitors users every 10 seconds in a background thread.
    """
    User = get_user_model()
    while True:
        users = User.objects.all()
        print(f"[MONITOR LOOP] Total users in system: {users.count()}")
        time.sleep(10)


def start_monitor():
    """
    Start a daemon thread to monitor users when Django boots.
    """
    thread = threading.Thread(target=monitor_users_loop, daemon=True)
    thread.start()


@shared_task
def monitor_users_task():
    """
    Celery task version to run on schedule (e.g., every 10 sec with Celery Beat).
    """
    User = get_user_model()
    user_count = User.objects.count()
    print(f"[CELERY MONITOR] Total users: {user_count}")
    return user_count
