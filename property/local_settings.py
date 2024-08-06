# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-#axl(v(=5s+4m9bswrz&$zxeljep=xr_1re2hx-v447ug^*%z6"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True  # Set to False in production

ALLOWED_HOSTS = [] # ["12.34.56.78"] # My app digital ocean ip address

# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "property",
        "USER": "postgres",
        "PASSWORD": "test",
        "HOST": "localhost",
    }
}

# Email config
EMAIL_HOST = "smtp.gmail.com"
EMAIL_PORT = 587
EMAIL_HOST_USER = "myemail@gmail.com"
EMAIL_HOST_PASSWORD = ""
EMAIL_USE_TLS = True
