from django.shortcuts import render
from django.http import JsonResponse, HttpResponseForbidden
from .models import Course, Theme
from django.contrib.auth.decorators import login_required
from django_ratelimit.decorators import ratelimit
from django.conf import settings
from django.core.exceptions import PermissionDenied
@ratelimit(key='ip', rate=settings.RATE_LIMIT)
def courses(request):
    if request.COUNTRY_CODE == "RU":
        return HttpResponseForbidden("Go away!")
    context = {
        'courses': Course.objects.all()
    }
    return render(request, "main/courses.html", context)
def ratelimit(request):
    raise PermissionDenied()
    
@ratelimit(key='ip', rate=settings.RATE_LIMIT)
@login_required
def themes(request, id):
    if request.COUNTRY_CODE == "RU":
        return HttpResponseForbidden("Go away!")
    context = {
        'course': Course.objects.get(pk=id)
    }
    return render(request, "main/presentations.html", context)

@ratelimit(key='ip', rate=settings.RATE_LIMIT)
def admin3(request):
    return render(request, "main/admin2.html", {'slug': ''})

@ratelimit(key='ip', rate=settings.RATE_LIMIT)
def admin2(request, slug):
    return render(request, "main/admin2.html", {'slug': slug})

@ratelimit(key='ip', rate=settings.RATE_LIMIT)
def header(request):
    return render(request, "main/header.html", {})


@ratelimit(key='ip', rate=settings.RATE_LIMIT)
@login_required
def test(request, id):
    if request.COUNTRY_CODE == "RU":
        return HttpResponseForbidden("Go away!")
    context = {
        'theme': Theme.objects.get(pk=id)
    }
    return render(request, "main/test.html", context)


@ratelimit(key='ip', rate=settings.RATE_LIMIT)
@login_required
def control_test(request, id):
    if request.COUNTRY_CODE == "RU":
        return HttpResponseForbidden("Go away!")
    context = {
        'course': Course.objects.get(pk=id)
    }
    return render(request, "main/control_test.html", context)


@ratelimit(key='ip', rate=settings.RATE_LIMIT)
def download(request):
    if request.COUNTRY_CODE == "RU":
        return HttpResponseForbidden("Go away!")
    return render(request, "main/download.html")


@ratelimit(key='ip', rate=settings.RATE_LIMIT)
@login_required
def presentation(request, id):
    if request.COUNTRY_CODE == "RU":
        return HttpResponseForbidden("Go away!")
    theme = Theme.objects.get(pk=id)
    context = {
        'theme': theme
    }
    return render(request, "main/presentation.html", context)

@ratelimit(key='ip', rate=settings.RATE_LIMIT)
@login_required
def check(request, id):
    if request.COUNTRY_CODE == "RU":
        return HttpResponseForbidden("Go away!")
    if request.method == 'POST':
        correct_test = {}
        score = 0
        correct_test_questions = []
        theme = Theme.objects.get(pk=id)
        test = theme.test
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
            'theme': theme
        }
        return render(request, "main/check.html", context)
    return JsonResponse({'message': 'Invalid request method'})

@ratelimit(key='ip', rate=settings.RATE_LIMIT)
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

@ratelimit(key='ip', rate=settings.RATE_LIMIT)
def update(request):
    if request.COUNTRY_CODE == "RU":
        return HttpResponseForbidden("Go away!")
    return JsonResponse({"latest": 20})

