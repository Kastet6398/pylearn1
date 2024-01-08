from django.shortcuts import render
from django.http import JsonResponse, HttpResponseForbidden
from .models import Course, Theme, Test
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.core.exceptions import PermissionDenied
import subprocess
import traceback
import time
import os
from django.http import HttpResponse
import cloudinary
import cloudinary.uploader
cloudinary.config( 
  cloud_name = "dkmvoezsb", 
  api_key = "453639488567156", 
  api_secret = "VerqaZWCdO2tioT2EBLb3dn0hrM" 
)


def calculator(request):
    if request.COUNTRY_CODE == "RU":
        return HttpResponseForbidden("Go away!")
    result = None
    if request.method == 'POST':
        expression = request.POST.get('expression', '')
        try:
            current_directory = os.path.dirname(os.path.abspath(__file__))
            jar_path = '/var/task/temp-1.0-SNAPSHOT'
            result_bytes = subprocess.check_output([jar_path, expression])
            result = result_bytes.decode('utf-8').strip()
        except:
            traceback.print_exc()
            result = "INTERNAL ERROR (500)"

    return render(request, 'main/calculator.html', {'result': result})

def keep_alive(request):
    return HttpResponse(status=204)

def courses(request):
    if request.COUNTRY_CODE == "RU":
        return HttpResponseForbidden("Go away!")
    courses = [i for i in Course.objects.all() if not(request.user != i.user and (i.choose_who_can_view_the_course and not (i.invited_users.all() and request.user in i.invited_users.all())))]
    context = {
        'courses': courses
    }
    return render(request, "main/courses.html", context)    

@login_required
def themes(request, id):
    if request.COUNTRY_CODE == "RU":
        return HttpResponseForbidden("Go away!")
    context = {
        'course': Course.objects.prefetch_related('invited_users', 'user').get(pk=id)
    }
    if request.user != context['course'].user and (context['course'].choose_who_can_view_the_course and not (context['course'].invited_users.all() and request.user in context['course'].invited_users.all())):
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
def theme(request, id):
    if request.COUNTRY_CODE == "RU":
        return HttpResponseForbidden("Go away!")
    context = {
        'theme': Theme.objects.get(pk=id)
    }
    return render(request, 'main/theme.html', context)

@login_required
def test(request, id):
    if request.COUNTRY_CODE == "RU":
        return HttpResponseForbidden("Go away!")
    context = {
        'test': Test.objects.get(pk=id)
    }
    return render(request, "main/test.html", context)


@login_required
def control_test(request, id):
    if request.COUNTRY_CODE == "RU":
        return HttpResponseForbidden("Go away!")
    context = {
        'course': Course.objects.get(pk=id)
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
def check(request, id):
    if request.COUNTRY_CODE == "RU":
        return HttpResponseForbidden("Go away!")
    if request.method == 'POST':
        correct_test = {}
        score = 0
        correct_test_questions = []
        test = Test.objects.get(pk=id)
        for question in test.questions.all():
            user_answer = request.POST.get(f"q{question.id}")
            correct_test_question = {}
            correct_test_question['question'] = question.question
            correct_test_question['answers'] = question.answers.all()
            correct_test_question['correct'] = question.correct.answer
            correct_test_question['selected'] = user_answer
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
def check_control(request, id):
    if request.COUNTRY_CODE == "RU":
        return HttpResponseForbidden("Go away!")
    if request.method == 'POST':
        correct_test = {}
        score = 0
        correct_test_questions = []
        course = Course.objects.get(pk=id)
        test = course.control_test
        for question in test.questions.all():
            user_answer = request.POST.get(f"q{question.id}")
            correct_test_question = {}
            correct_test_question['question'] = question.question
            correct_test_question['answers'] = question.answers.all()
            correct_test_question['correct'] = question.correct.answer
            correct_test_question['selected'] = user_answer
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

