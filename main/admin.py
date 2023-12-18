from django.contrib import admin
from .models import Course, Theme, Test, Question, Answer

admin.site.register(Course)
admin.site.register(Theme)
admin.site.register(Question)
admin.site.register(Answer)
admin.site.register(Test)