from django.shortcuts import render
from .models import Question, Choice

# Create your views here.


def index(request):
    questions = Question.objects.all()
    # print(questions)
    context = {
        'questions': questions
    }
    return render(request, 'polls/index.html', context)
