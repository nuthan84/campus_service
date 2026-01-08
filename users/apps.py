from django.apps import AppConfig
from django.contrib.auth import get_user_model
import os

class UsersConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'users'

    def ready(self):
        User = get_user_model()
        if os.environ.get("CREATE_ADMIN_USER", "False") == "True":
            if not User.objects.filter(username="admin").exists():
                User.objects.create_superuser(
                    username="admin",
                    email="admin@example.com",
                    password="Admin@123"
                )
