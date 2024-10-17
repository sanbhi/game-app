from django.shortcuts import render
from .models import Question
import random

def quiz(request):
    questions = list(Question.objects.all())
    random.shuffle(questions)
    return render(request, 'quiz/quiz.html', {'questions': questions[:5]})  # Show 5 questions

def result(request):
    score = 0
    for question in Question.objects.all():
        if str(question.correct_answer) == request.POST.get(str(question.id)):
            score += 1
    return render(request, 'quiz/result.html', {'score': score})
