from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout


def landing_page(request):
    return render(request, "app/landing__page.html")


@login_required
def dashboard_landing_page(request):
    return render(request, "app/dashboard.html")


@login_required
def update_soldier_readiness(request):
    return render(request, "app/update_readiness.html")


@login_required
def protected_view(request):
    return render(request, "app/profile.html")


def logout_view(request):
    logout(request)
    return redirect("account_login")
