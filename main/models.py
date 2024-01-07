from django.db import models
from django.contrib.auth.models import User
from django.contrib.postgres.fields import ArrayField

class Answer(models.Model):
    answer = models.TextField()

    def __str__(self):
        return self.answer

class RateLimit(models.Model):
    ip_address = models.GenericIPAddressField()
    timestamp = models.DateTimeField(auto_now_add=True)
    connection_number = models.PositiveIntegerField(default=0)

class AdditionalResource(models.Model):
    url = models.URLField()
    title = models.CharField(max_length=1000)

    def __str__(self):
        return self.title

class Question(models.Model):
    question = models.TextField()
    answers = models.ManyToManyField(Answer)
    correct = models.ForeignKey(Answer, on_delete=models.CASCADE, related_name="correct")

    def __str__(self):
        return self.question

class Test(models.Model):
    questions = models.ManyToManyField(Question)

    def __str__(self):
        return str(self.id)

class Theme(models.Model):
    name = models.CharField(max_length=255)
    test = models.ForeignKey(Test, on_delete=models.CASCADE, blank=True, null=True)
    video_meeting = models.URLField(blank=True, null=True)
    position_in_themes_list = models.IntegerField()
    description = models.TextField(blank=True, null=True)
    additional_resources = models.ManyToManyField(AdditionalResource)

    class Meta:
        ordering = ['position_in_themes_list']

    def __str__(self):
        return self.name

class Course(models.Model):
    themes = models.ManyToManyField(Theme)
    name = models.CharField(max_length=255)
    invited_users = models.ManyToManyField(User, blank=True, null=True)
    choose_who_can_view_the_course = models.BooleanField(default=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='created', blank=True, null=True)
    control_test = models.ForeignKey(Test, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.name
