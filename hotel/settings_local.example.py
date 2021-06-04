SECRET_KEY = 'secret-key'

DEBUG = True

ALLOWED_HOSTS = ['*']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'db_name',
        'USER': 'db_user',
        'HOST': 'localhost',
        'PASSWORD': 'db_password',
        'PORT': 5432
    }
}
