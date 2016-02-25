from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


def login_view(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user is not None:
        if user.is_active:
            login(request, user)
            return profile(request)
        else:
            # Return a 'disabled account' error message
            return render(request, template_name='demo.html')
    else:
        # Return an 'invalid login' error message.
        return render(request, template_name='demo.html')


def logout_view(request):
    logout(request)

# @login_required
# TODO add login functionality, https://docs.djangoproject.com/en/1.9/topics/auth/default/#django.contrib.auth.decorators.login_required
def profile(request):
    return render(request, template_name='demo.html')
