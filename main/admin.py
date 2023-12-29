from django.contrib import admin
from .models import Course, Theme, Test, Question, Answer

class CourseAdmin(admin.ModelAdmin):
    list_per_page = 15

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

class ThemeAdmin(admin.ModelAdmin):
    list_per_page = 15

class QuestionAdmin(admin.ModelAdmin):
    list_per_page = 15

class AnswerAdmin(admin.ModelAdmin):
    list_per_page = 15

class TestAdmin(admin.ModelAdmin):
    list_per_page = 15

admin.site.register(Course, CourseAdmin)
admin.site.register(Theme, ThemeAdmin)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Answer, AnswerAdmin)
admin.site.register(Test, TestAdmin)
