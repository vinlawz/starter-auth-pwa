from django.urls import path
from .views import landing_page, dashboard_landing_page, update_soldier_readiness, protected_view, logout_view

app_name = "app"

urlpatterns = [
    path("", landing_page, name="index"),
    path("dashboard/", dashboard_landing_page, name="dashboard_landing_page"),  # Ensure this exists
    path("update-readiness/", update_soldier_readiness, name="update_soldier_readiness"),
    path("protected/", protected_view, name="protected_view"),
    path("logout/", logout_view, name="logout"),
]