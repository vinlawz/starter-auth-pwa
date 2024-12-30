from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import UserCreationForm, UserChangeForm
from .models import User, UserProfile

class UserProfileInline(admin.StackedInline):  # new
    model = UserProfile
    can_delete = False
    verbose_name_plural = "User Profile"

class UserAdmin(UserAdmin):
    add_form = UserCreationForm
    form = UserChangeForm
    model = User
    list_display = (
        "email",
        "is_staff",
        "is_active",
        "is_verified",
    )
    list_filter = (
        "is_verified",
        "is_active",
    )
    fieldsets = (
        ("Confidential", {"fields": ("email", "password",)}),
        ("General Information", {"fields": ("first_name", "last_name")}),
        (
            "Permissions",
            {"fields": ("is_staff", "is_active", "is_verified", "groups", "user_permissions")},
        ),
    )
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
    inlines = [UserProfileInline]

    

@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ("user", )
    
    
admin.site.register(User, UserAdmin)