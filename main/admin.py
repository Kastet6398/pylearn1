from django.contrib import admin
from .models import Course, Theme, Test, Question, Answer

class CourseAdmin(admin.ModelAdmin):
    list_per_page = 15

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
