from cloudinary.models import CloudinaryField
from django.contrib.auth.models import User
from django.db import models


class BaseModel(models.Model):
    objects = models.Manager()

    class Meta:
        abstract = True

    def __str__(self):
        # noinspection PyUnresolvedReferences
        return str(self.id)


class Answer(BaseModel):
    answer = models.TextField()

    def __str__(self):
        return self.answer


class RateLimit(BaseModel):
    ip_address = models.GenericIPAddressField()
    timestamp = models.DateTimeField(auto_now_add=True)
    connection_number = models.PositiveIntegerField(default=0)


class AdditionalResource(BaseModel):
    url = models.URLField()
    title = models.CharField(max_length=1000)

    def __str__(self):
        return self.title


class Question(BaseModel):
    question = models.TextField()
    answers = models.ManyToManyField(Answer)
    correct = models.ForeignKey(Answer, on_delete=models.CASCADE, related_name="correct")

    def __str__(self):
        return self.question


class Test(BaseModel):
    questions = models.ManyToManyField(Question)


class Attachment(BaseModel):
    file = CloudinaryField(
        resource_type="auto",
    )

    search_fields = ['file__icontains']


class HomeWork(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    theme = models.ForeignKey('Theme', on_delete=models.CASCADE)
    attachments = models.ManyToManyField(Attachment)


class Theme(BaseModel):
    name = models.CharField(max_length=255)
    test = models.ForeignKey(Test, on_delete=models.CASCADE, blank=True, null=True)
    video_meeting = models.URLField(blank=True, null=True)
    position_in_themes_list = models.IntegerField()
    description = models.TextField(blank=True, null=True)
    additional_resources = models.ManyToManyField(AdditionalResource)
    has_homework = models.BooleanField(default=False)

    class Meta:
        ordering = ['position_in_themes_list']

    def __str__(self):
        return self.name


class Course(BaseModel):
    themes = models.ManyToManyField(Theme)
    name = models.CharField(max_length=255)
    invited_users = models.ManyToManyField(User, blank=True, null=True)
    choose_who_can_view_the_course = models.BooleanField(default=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='created', blank=True, null=True)
    control_test = models.ForeignKey(Test, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.name
