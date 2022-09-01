from django.shortcuts import get_object_or_404,render
from django.views.decorators.csrf import csrf_protect

from .models import Course as Kursevi,Articles
from .forms import CourseForm,ArticleForm
# Create your views here.
@csrf_protect
def addCourse(request):

    return render(request, 'add.html', {'form': CourseForm})
@csrf_protect
def addArticle(request):

    return render(request, 'addArticle.html', {'form': ArticleForm})
@csrf_protect
def index(request):
    return render(request, 'index.html')
@csrf_protect
def Course(request):
    queryset = Kursevi.objects.filter(author=request.user).all()
    context = {"courses": queryset}
    return render(request, 'courses.html', context)
@csrf_protect
def Article(request):
    queryset = Articles.objects.filter(author=request.user).all()
    context = {"articles": queryset}
    return render(request, 'articles.html', context)
def quiz(request):
    return render(request, 'quiz.html')