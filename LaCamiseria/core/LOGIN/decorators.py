from django.contrib.auth.decorators import user_passes_test

def user_authenticated(user):
    return user.is_authenticated

# Decorador personalizado
authenticated = user_passes_test(user_authenticated)