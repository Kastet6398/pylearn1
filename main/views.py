import subprocess
import traceback

import cloudinary
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.http import JsonResponse, HttpResponseForbidden
from django.shortcuts import render, redirect

from .forms import HomeWorkForm
from .models import Course, Theme, Test, Attachment, HomeWork

cloudinary.config(
    cloud_name="dkmvoezsb",
    api_key="453639488567156",
    api_secret="VerqaZWCdO2tioT2EBLb3dn0hrM"
)


def home_work_create_view(request):
    if request.method == 'POST':
        form = HomeWorkForm(request.POST)
        files = request.FILES.getlist('attachments')

        if 'attachments' not in request.FILES or not form.is_valid():
            return redirect('index')

        retrieved_theme = Theme.objects.get(pk=int(request.POST['theme']))
        user = request.user

        home_work_instance = HomeWork(theme=retrieved_theme, user=user)
        home_work_instance.save()

        for file in files:
            print(file)
            attachment_instance = Attachment.objects.create(file=file)
            home_work_instance.attachments.add(attachment_instance)

        home_work_instance.save()

        return redirect(request.path_info)
    else:
        form = HomeWorkForm()

    return render(request, 'main/home_work.html', {'form': form})


def ggg(request):
    return render(request, 'main/ggg.html', {})


def calculator(request):
    if request.COUNTRY_CODE == "RU":
        return HttpResponseForbidden("Go away!")
    result = None
    if request.method == 'POST':
        expression = request.POST.get('expression', '')
        try:
            jar_path = '/var/task/temp-1.0-SNAPSHOT'
            result_bytes = subprocess.check_output([jar_path, expression])
            result = result_bytes.decode('utf-8').strip()
        except (Exception,):
            traceback.print_exc()
            result = "INTERNAL ERROR (500)"

    return render(request, 'main/calculator.html', {'result': result})


# noinspection PyUnusedLocal
def keep_alive(request):
    return HttpResponse(status=204)


def courses(request):
    if request.COUNTRY_CODE == "RU":
        return HttpResponseForbidden("Go away!")
    retrieved_courses = [i for i in Course.objects.all() if not (request.user != i.user and (
            i.choose_who_can_view_the_course and not (
                i.invited_users.all() and request.user in i.invited_users.all())))]
    context = {
        'courses': retrieved_courses
    }
    return render(request, "main/courses.html", context)


@login_required
def themes(request, object_id):
    if request.COUNTRY_CODE == "RU":
        return HttpResponseForbidden("Go away!")
    context = {
        'course': Course.objects.prefetch_related('invited_users', 'user').get(pk=object_id)
    }
    if request.user != context['course'].user and (context['course'].choose_who_can_view_the_course and not (
            context['course'].invited_users.all() and request.user in context['course'].invited_users.all())):
        return HttpResponseForbidden("You don't have permission to view this course.")
    return render(request, "main/presentations.html", context)


def admin3(request):
    if request.COUNTRY_CODE == "RU":
        return HttpResponseForbidden("Go away!")
    return render(request, "main/admin2.html", {'slug': ''})


def admin2(request, slug):
    if request.COUNTRY_CODE == "RU":
        return HttpResponseForbidden("Go away!")
    return render(request, "main/admin2.html", {'slug': slug})


def header(request):
    if request.COUNTRY_CODE == "RU":
        return HttpResponseForbidden("Go away!")
    return render(request, "main/header.html", {})


@login_required
def theme(request, object_id):
    if request.COUNTRY_CODE == "RU":
        return HttpResponseForbidden("Go away!")

    homework_form = HomeWorkForm()
    retrieved_theme = Theme.objects.get(pk=object_id)

    if request.method == 'POST':
        homework_form = HomeWorkForm(request.POST, request.FILES)
        if homework_form.is_valid():
            user = request.user

            homework = HomeWork(theme=retrieved_theme, user=user)
            homework.save()

            for file in request.FILES.getlist('attachments'):
                attachment = Attachment.objects.create(file=file)
                homework.attachments.add(attachment)

            return redirect(f'/theme/{object_id}')

    context = {
        'theme': retrieved_theme,
        'hw_form': homework_form
    }
    return render(request, 'main/theme.html', context)


@login_required
def test(request, object_id):
    if request.COUNTRY_CODE == "RU":
        return HttpResponseForbidden("Go away!")
    context = {
        'test': Test.objects.get(pk=object_id)
    }
    return render(request, "main/test.html", context)


@login_required
def control_test(request, object_id):
    if request.COUNTRY_CODE == "RU":
        return HttpResponseForbidden("Go away!")
    context = {
        'course': Course.objects.get(pk=object_id)
    }
    return render(request, "main/control_test.html", context)


def download(request):
    if request.COUNTRY_CODE == "RU":
        return HttpResponseForbidden("Go away!")
    return render(request, "main/download.html")


def embed(request, resource):
    if request.COUNTRY_CODE == "RU":
        return HttpResponseForbidden("Go away!")
    context = {
        'resource': resource
    }
    return render(request, "main/embed.html", context)


@login_required
def check(request, object_id):
    if request.COUNTRY_CODE == "RU":
        return HttpResponseForbidden("Go away!")
    if request.method == 'POST':
        correct_test = {}
        score = 0
        correct_test_questions = []
        retrieved_test = Test.objects.get(pk=object_id)
        for question in retrieved_test.questions.all():
            user_answer = request.POST.get(f"q{question.object_id}")
            correct_test_question = {'question': question.question, 'answers': question.answers.all(),
                                     'correct': question.correct.answer, 'selected': user_answer}
            correct_test_questions.append(correct_test_question)
            if user_answer == question.correct.answer:
                score += 1
        correct_test['questions'] = correct_test_questions
        context = {
            'test': correct_test,
            'questions_length': len(correct_test_questions),
            'score': score,
        }
        return render(request, "main/check.html", context)
    return JsonResponse({'message': 'Invalid request method'})


@login_required
def check_control(request, object_id):
    if request.COUNTRY_CODE == "RU":
        return HttpResponseForbidden("Go away!")
    if request.method == 'POST':
        correct_test = {}
        score = 0
        correct_test_questions = []
        course = Course.objects.get(pk=object_id)
        retrieved_test = course.control_test
        for question in retrieved_test.questions.all():
            user_answer = request.POST.get(f"q{question.object_id}")
            correct_test_question = {'question': question.question, 'answers': question.answers.all(),
                                     'correct': question.correct.answer, 'selected': user_answer}
            correct_test_questions.append(correct_test_question)
            if user_answer == question.correct.answer:
                score += 1
        correct_test['questions'] = correct_test_questions
        context = {
            'test': correct_test,
            'questions_length': len(correct_test_questions),
            'score': score,
            'course': course
        }
        return render(request, "main/check_control.html", context)
    return JsonResponse({'message': 'Invalid request method'})


def update(request):
    if request.COUNTRY_CODE == "RU":
        return HttpResponseForbidden("Go away!")
    return JsonResponse({"latest": 20})
