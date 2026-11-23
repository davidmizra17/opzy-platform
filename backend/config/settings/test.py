from .base import *  # noqa: F403
from .base import env

DATABASES = {
    "default": env.db("DATABASE_URL", default="sqlite:///:memory:"),
}
CELERY_TASK_ALWAYS_EAGER = True
PASSWORD_HASHERS = ["django.contrib.auth.hashers.MD5PasswordHasher"]
REST_FRAMEWORK = {
    **REST_FRAMEWORK,  # noqa: F405
    "DEFAULT_THROTTLE_CLASSES": [],
}
