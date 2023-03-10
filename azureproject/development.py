import os
from pathlib import Path

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.getenv('SECRET_KEY', 'flask-insecure-7ppocbnx@w71dcuinn*t^_mzal(t@o01v3fee27g%rg18fc5d@')

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

DATABASE_URI = 'mysql://{dbuser}:{dbpass}@{dbhost}/{dbname}'.format(
    dbuser='robert.tracey',
    dbpass='i.r8D8UgyeltJ_wC',
    dbhost='localhost',
    dbname='python_sample'
)

TIME_ZONE = 'UTC'

STATICFILES_DIRS = (str(BASE_DIR.joinpath('static')),)
STATIC_URL = 'static/'

