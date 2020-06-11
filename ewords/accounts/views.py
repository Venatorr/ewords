from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.views import LoginView
from django.urls import reverse


class CustomLoginView(LoginView):
    template_name = 'auth/login.html'

    def get_success_url(self):
        if self.request.user.is_superuser:
            return reverse("index")
        else:
            return reverse("index")


def logout_view(request):
    logout(request)
    return redirect("index")


def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('index')
    else:
        form = UserCreationForm()
    context = {'form': form}
    return render(request, "auth/register.html", context)
