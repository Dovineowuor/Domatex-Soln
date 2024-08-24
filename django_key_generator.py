import secrets

def generate_django_secret_key():
    secret = secrets.token_urlsafe(50)
    return f'django-secret+{secret}'

print(generate_django_secret_key())