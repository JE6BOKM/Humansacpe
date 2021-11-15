import os

import dj_database_url

from .common import Common

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


class Local(Common):
    DEBUG = True

    # Testing
    INSTALLED_APPS = Common.INSTALLED_APPS
    # django extensions
    INSTALLED_APPS += (
        # django extensions
        "django_extensions",
    )

    # Mail
    EMAIL_HOST = "localhost"
    EMAIL_PORT = 1025
    EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"

    REST_FRAMEWORK = Common.REST_FRAMEWORK
    REST_FRAMEWORK["DEFAULT_AUTHENTICATION_CLASSES"] = [  # noqa
        "apps.core.authentications.AutoLoginAuthentication",
    ]

    LOCAL_DB_PATH = Common.LOCAL_DB_PATH
    DATABASES = {
        "default": dj_database_url.config(default=f"sqlite://///{LOCAL_DB_PATH}")
    }
