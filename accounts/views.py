from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth import logout
from django.db.models.manager import Manager
from .forms import CustomUserCreationForm, CompanyForm
from .models import Company

Company.objects: Manager  # type: ignore

def home(request):
    return render(request, 'accounts/home.html')

def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}! Please complete your company profile.')
            return redirect('company_profile')
    else:
        form = CustomUserCreationForm()
    return render(request, 'accounts/signup.html', {'form': form})

@login_required
def company_profile(request):
    try:
        company = Company.objects.get(user=request.user)  # type: ignore
        if company.is_profile_completed:
            return redirect('dashboard')
    except Company.DoesNotExist:  # type: ignore
        company = None

    if request.method == 'POST':
        form = CompanyForm(request.POST, instance=company)
        if form.is_valid():
            company = form.save(commit=False)
            company.user = request.user
            company.is_profile_completed = True
            company.save()
            return render(request, 'accounts/company_profile.html', {
                'show_reward': True,
                'form': CompanyForm(instance=company)  # Send a fresh form
            })
    else:
        form = CompanyForm(instance=company)
    
    return render(request, 'accounts/company_profile.html', {'form': form})

@login_required
def dashboard(request):
    try:
        company = Company.objects.get(user=request.user)  # type: ignore
        if not company.is_profile_completed:
            messages.warning(request, 'Please complete your company profile.')
            return redirect('company_profile')
    except Company.DoesNotExist:  # type: ignore
        messages.warning(request, 'Please complete your company profile.')
        return redirect('company_profile')
    
    return render(request, 'accounts/dashboard.html', {'company': company})

def logout_view(request):
    logout(request)
    messages.success(request, 'You have been successfully logged out.')
    return redirect('home')
