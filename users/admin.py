from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _

from .forms import UserCreationForm, UserChangeForm
from .models import User, EndUserProfile, StaffUserProfile

# Inline admin for profiles
class StaffUserProfileInline(admin.StackedInline):
    model = StaffUserProfile
    can_delete = False
    verbose_name_plural = "Staff Profiles"

class EndUserProfileInline(admin.StackedInline):
    model = EndUserProfile
    can_delete = False
    verbose_name_plural = "End User Profiles"

class CustomUserAdmin(UserAdmin):
    add_form = UserCreationForm
    form = UserChangeForm
    model = User

    # Displayed fields in the admin list view
    list_display = (
        "email",
        "type",
        "is_staff",
        "is_active",
        "is_verified",
    )
    list_filter = (
        "type",
        "is_verified",
        "is_active",
    )

    # Fieldsets for viewing/editing a user
    fieldsets = (
        (_("Credentials"), {"fields": ("email", "password")}),
        (_("Personal Info"), {"fields": ("first_name", "last_name")}),
        (
            _("Permissions"),
            {"fields": ("is_staff", "is_active", "is_verified", "is_superuser", "groups", "user_permissions")},
        ),
        (_("User Type"), {"fields": ("type",)}),
    )

    # Fieldsets for creating a new user
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": (
                    "email",
                    "first_name",
                    "last_name",
                    "password1",
                    "password2",
                    "type",
                    "is_staff",
                    "is_active",
                    "groups",
                    "user_permissions",
                ),
            },
        ),
    )

    search_fields = ("email", "first_name", "last_name")
    ordering = ("email",)

    # Dynamically include the correct inline based on user type
    def get_inlines(self, request, obj=None):
        if obj:
            if obj.type == User.Types.STAFF:
                return [StaffUserProfileInline]
            elif obj.type == User.Types.ENDUSER:
                return [EndUserProfileInline]
        return []

# Register the custom User model and admin
admin.site.register(User, CustomUserAdmin)

# Admin for Staff and End User Profiles
@admin.register(StaffUserProfile)
class StaffUserProfileAdmin(admin.ModelAdmin):
    list_display = ("user",)
    search_fields = ("user__email", "user__first_name", "user__last_name")

@admin.register(EndUserProfile)
class EndUserProfileAdmin(admin.ModelAdmin):
    list_display = ("user",)
    search_fields = ("user__email", "user__first_name", "user__last_name")