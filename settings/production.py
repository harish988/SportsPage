from .base import 
import dj_database_url

ENVIRONMENT = 'production'
DEBUG = False
ALLOWED_HOSTS = ['']
DATABASES['default'] = dj_database_url.config(
    default='DATABASE_URL_HERE'
)