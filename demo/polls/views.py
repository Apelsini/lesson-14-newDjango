from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, Http404
from .models import Question, Choice

# Create your views here.
def index(request):
    questions_list = Question.objects.order_by('-update_date')[:5]
    context = {
        'questions_list': questions_list,
    }
    return render(request=request, template_name='polls/index.html', context=context)

def detail(request, question_id):
    try:
        question = Question.objects.get(id=question_id)
    except Question.DoesNotExist:
        raise Http404("Question you are trying to get does not exist!")
    return render(request,'polls/detail.html', {'question': question, 'choices': [q for q in question.choice_set.all()]})

def results_view(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    choices = [c for c in question.choice_set.all()]
    return render(request, 'polls/results.html', {'question': question, 'choices': choices})

def vote(request, choice_id):
    choice = get_object_or_404(Choice, pk=choice_id)
    choice.votes += 1
    choice.save()
    q_id = choice.question.id
    return redirect('/polls/'+ str(q_id) + "/results/")