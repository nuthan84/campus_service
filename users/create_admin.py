from django.contrib.auth import get_user_model

User = get_user_model()

if not User.objects.filter(username="nuthan").exists():
    User.objects.create_superuser(
        username="nuthan",
        password="nuthan84",
        email="nuthanuthejvalluri@gmail.com"
    )
