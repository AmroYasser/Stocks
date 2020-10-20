from django.shortcuts import render, redirect
from django.contrib import messages

from .forms import UserRegisterForm
from .serializers import UserSerializer


def register(request):
    """
        Create new user
    """
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'register.html', {'form': form})


def get_my_profile(request):
    """
        Create new user
    """
    user = UserSerializer(request.user)
    return render(request, 'profile.html', {'user': user.data})
