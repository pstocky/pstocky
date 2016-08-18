# -*- coding:utf-8 -*-
from django import forms
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.contrib.auth.models import Group

from .models import MyUser, Token


class UserCreationForm(forms.ModelForm):
    """A form for creating new users. Includes all the required
    fields, plus a repeated password."""
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)

    class Meta:
        model = MyUser
        fields = (
            'username', 'password1', 'password2',
        )

    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super(UserCreationForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


class UserChangeForm(forms.ModelForm):
    """A form for updating users. Includes all the fields on
    the user, but replaces the password field with admin's
    password hash display field.
    """
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = MyUser
        fields = ('username', 'password', 'is_staff')

    def clean_password(self):
        # Regardless of what the user provides, return the initial value.
        # This is done here, rather than on the field, because the
        # field does not have access to the initial value
        return self.initial["password"]


@admin.register(MyUser)
class UserAdmin(BaseUserAdmin):
    # The forms to add and change user instances
    form = UserChangeForm
    add_form = UserCreationForm

    def avatar_img(self, ins):
        return '<img src="%s" title="%s"/>' % (
            ins.avatar.url, ins.nick_name)

    avatar_img.short_description = u"头像预览"
    avatar_img.allow_tags = True

    # The fields to be used in displaying the User model.
    # These override the definitions on the base UserAdmin
    # that reference specific fields on auth.User.
    list_display = (
        'avatar_img',
        'username', 'nick_name', 'offical_name',
        'role', 'status',
        'gender',
        'is_staff',
    )

    list_filter = (
        'role', 'status',
        'hide_offical_name',
        'is_staff', 'gender',
    )

    fieldsets = (
        (None, {
            'fields': (
                'avatar_img', 'avatar',
                'username',
                'role',
                'status',
                'password',
            ),
        }),
        (u'基本信息', {
            'fields': (
                'nick_name',
                'offical_name', 'hide_offical_name',
                'gender',
            ),
        }),
        (u'角色权限', {
            'fields': (
                'is_staff',
            ),
        }),
    )

    readonly_fields = ('avatar_img', )

    # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    # overrides get_fieldsets to use this attribute when creating a user.
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': (
                'username', 'password1', 'password2',
            )
        }),
    )
    search_fields = (
        'username',
        'nick_name',
        'offical_name',
    )
    ordering = (
        'username',
    )
    filter_horizontal = ()


@admin.register(Token)
class TokenAdmin(admin.ModelAdmin):
    list_display = (
        'key', 'user',
        'user_agent', 'created_at',
    )

    search_fields = (
        'key',
    )


# ... and, since we're not using Django's built-in permissions,
# unregister the Group model from admin.
admin.site.unregister(Group)
