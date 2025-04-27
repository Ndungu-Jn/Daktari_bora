from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib import messages
from .forms import UserRegistrationForm


def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Log the user in after registration
            login(request, user)
            messages.success(request, f"Account created successfully! Welcome, {user.first_name}!")
            return redirect('client_list')  # Redirect to client list or your home page
    else:
        form = UserRegistrationForm()
    
    return render(request, 'accounts/register.html', {'form': form})