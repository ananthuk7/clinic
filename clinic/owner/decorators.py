from django.shortcuts import redirect


def admin_login(func):
    def wrapper(request, id=None, *args, **kwargs):
        if request.user.is_superuser:
            redirect('dashboard')
        else:
            return func(request, id, *args, **kwargs)

    return wrapper
