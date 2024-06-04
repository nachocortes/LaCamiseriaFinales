from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib import messages
from .forms import SignUpForm, EditProfileForm
from ..CRM.models import Cliente


def perfil_user(request):
    return render(request, 'login/perfil_usuario.html', {})


def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            # Crear Cliente si no existe
            if not Cliente.objects.filter(user=user).exists():
                Cliente.objects.create(user=user, nombre=user.username, email=user.email)
            messages.success(request, 'Has iniciado sesión')
            return redirect('perfil_usuario')
        else:
            messages.error(request, 'Error al iniciar sesión')
            return redirect('login')
    else:
        return render(request, 'login/login.html', {})


def logout_user(request):
    logout(request)
    messages.success(request, 'Ahora estás desconectado')
    return redirect('perfil_usuario')


def register_user(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            Cliente.objects.create(user=user, nombre=user.username, email=user.email)
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            if user is not None:
                login(request, user)
                messages.success(request, 'Te has registrado exitosamente.')
                return redirect('store:inicioStore')
            else:
                messages.error(request, 'Error en la autenticación. Por favor, intente nuevamente.')
    else:
        form = SignUpForm()
    return render(request, 'login/register.html', {'form': form})


def edit_profile(request):
    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Has editado tu perfil')
            return redirect('perfil_usuario')
    else:
        form = EditProfileForm(instance=request.user)

    context = {'form': form}
    return render(request, 'login/edit_profile.html', context)


def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(data=request.POST, user=request.user)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            messages.success(request, 'Has editado tu contraseña')
            return redirect('perfil_usuario')
    else:
        form = PasswordChangeForm(user=request.user)

    context = {'form': form}
    return render(request, 'login/change_password.html', context)