from django.contrib import admin

from .models import Course, Theme, Test, Question, Answer, AdditionalResource, HomeWork, Attachment


# from admin_site_search.views import AdminSiteSearchView


class AdditionalResourceAdmin(admin.ModelAdmin):
    search_fields = ["title"]
    exclude = ["user"]

    def get_model_perms(self, request):
        return {}

    def has_change_permission(self, request, obj=None):
        return not (obj is not None and obj.user != request.user)

    def has_delete_permission(self, request, obj=None):
        return self.has_change_permission(request, obj)

    def save_model(self, request, obj, form, change):
        obj.user = request.user
        super().save_model(request, obj, form, change)


class CourseAdmin(admin.ModelAdmin):
    list_per_page = 15
    exclude = ["user"]
    search_fields = ["name"]

    def has_change_permission(self, request, obj=None):
        return not (obj is not None and obj.user != request.user)

    def has_delete_permission(self, request, obj=None):
        return self.has_change_permission(request, obj)

    fieldsets = (
        ('Main', {
            'fields': ('name', 'themes', 'control_test')
        }),
        ('Security', {
            'fields': ('choose_who_can_view_the_course', 'invited_users')
        }),
    )

    class Media:
        js = ("admin/js/toggleInvitedUsersField.js",)

    def save_model(self, request, obj, form, change):
        obj.user = request.user
        super().save_model(request, obj, form, change)


class HomeWorkAdmin(admin.ModelAdmin):
    list_per_page = 15
    exclude = ["user"]
    search_fields = ["id"]

    fields = ['attachments', 'theme']

    def has_change_permission(self, request, obj=None):
        return not (obj is not None and obj.user != request.user)

    def has_delete_permission(self, request, obj=None):
        return self.has_change_permission(request, obj)

    def save_model(self, request, obj, form, change):
        obj.user = request.user
        super().save_model(request, obj, form, change)


class ThemeAdmin(admin.ModelAdmin):
    autocomplete_fields = ['additional_resources']
    list_per_page = 15
    exclude = ["user"]
    search_fields = ["name"]

    def has_change_permission(self, request, obj=None):
        return not (obj is not None and obj.user != request.user)

    def has_delete_permission(self, request, obj=None):
        return self.has_change_permission(request, obj)

    def save_model(self, request, obj, form, change):
        obj.user = request.user
        super().save_model(request, obj, form, change)


class QuestionAdmin(admin.ModelAdmin):
    list_per_page = 15
    exclude = ["user"]
    search_fields = ["question"]

    def get_model_perms(self, request):
        return {}

    def has_change_permission(self, request, obj=None):
        return not (obj is not None and obj.user != request.user)

    def has_delete_permission(self, request, obj=None):
        return self.has_change_permission(request, obj)

    def save_model(self, request, obj, form, change):
        obj.user = request.user
        super().save_model(request, obj, form, change)


class AnswerAdmin(admin.ModelAdmin):
    list_per_page = 15
    exclude = ["user"]
    search_fields = ["answer"]

    def get_model_perms(self, request):
        return {}

    def has_change_permission(self, request, obj=None):
        return not (obj is not None and obj.user != request.user)

    def has_delete_permission(self, request, obj=None):
        return self.has_change_permission(request, obj)

    def save_model(self, request, obj, form, change):
        obj.user = request.user
        super().save_model(request, obj, form, change)


class TestAdmin(admin.ModelAdmin):
    list_per_page = 15
    exclude = ["user"]
    search_fields = ["id"]

    def has_change_permission(self, request, obj=None):
        return not (obj is not None and obj.user != request.user)

    def has_delete_permission(self, request, obj=None):
        return self.has_change_permission(request, obj)

    def save_model(self, request, obj, form, change):
        obj.user = request.user
        super().save_model(request, obj, form, change)


class AttachmentAdmin(admin.ModelAdmin):
    list_per_page = 15
    exclude = ["user"]
    search_fields = ["id"]

    def get_model_perms(self, request):
        return {}

    def has_change_permission(self, request, obj=None):
        return not (obj is not None and obj.user != request.user)

    def has_delete_permission(self, request, obj=None):
        return self.has_change_permission(request, obj)

    def save_model(self, request, obj, form, change):
        obj.user = request.user
        super().save_model(request, obj, form, change)


#    autocomplete_fields = ['questions']
admin.site.register(Attachment, AttachmentAdmin)
admin.site.register(HomeWork, HomeWorkAdmin)
admin.site.register(Course, CourseAdmin)
admin.site.register(Theme, ThemeAdmin)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Answer, AnswerAdmin)
admin.site.register(Test, TestAdmin)
admin.site.register(AdditionalResource, AdditionalResourceAdmin)
