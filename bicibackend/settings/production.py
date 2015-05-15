from bicibackend.settings.base import *


DEBUG = False

#ALLOWED_HOSTS = ['.example.com']
ALLOWED_HOSTS = ['*']


# Use the cached template loader so template is compiled once and read from
# memory instead of reading from disk on each load.
# TEMPLATES[0]['OPTIONS']['loaders'] = [
#     ('django.template.loaders.cached.Loader', [
#         'django.template.loaders.filesystem.Loader',
#         'django.template.loaders.app_directories.Loader',
#     ]),
# ]

DATABASES = {
    'default': {
        'ENGINE': 'django.contrib.gis.db.backends.postgis',
        'NAME': os.getenv('DATABASE_NAME', 'biciguia'),
        'USER': os.getenv('DATABASE_USER', 'biciguia'),
        'PASSWORD': os.getenv('DATABASE_PASSWORD', 'whatever'),
        'HOST': os.getenv('DATABASE_HOST', '127.0.0.1'),
        'PORT': os.getenv('DATABASE_PORT', '5432'),
    }
}