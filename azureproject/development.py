import os
from pathlib import Path

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

