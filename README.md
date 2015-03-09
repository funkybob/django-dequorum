# django-dequorum
A simple web forum for Django

# Installation

1. pip install django-dequorum
2. Add  "dequorum" to INSTALLED_APPS.
3. Add "dequorum.urls" to your url tree.

## Using the provided accounts app

1. Add "accounts" to INSTALLED_APPS
   If you want to use the provided login/logout templates you must put 'accounts' before 'django.contrib.auth' in INSTALLED_APPS.
2. Set AUTH_USER_MODEL = 'accounts.User'
3. Add "accounts.urls" to your url tree, ideally as:
    url(r'^accounts/', include('accounts.urls', namespace='accounts')),
