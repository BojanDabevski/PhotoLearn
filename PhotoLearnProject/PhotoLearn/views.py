from django.shortcuts import render
from .models import Course as Kursevi,Articles
from .forms import CourseForm,ArticleForm
# Create your views here.
def addCourse(request):

    return render(request, 'add.html', {'form': CourseForm})

def addArticle(request):

    return render(request, 'addArticle.html', {'form': ArticleForm})
def index(request):
    return render(request, 'index.html')

def Course(request):
    queryset = Kursevi.objects.filter(author=request.user).all()
    context = {"courses": queryset}
    return render(request, 'courses.html', context)

def Article(request):
    queryset = Articles.objects.filter(author=request.user).all()
    context = {"articles": queryset}
    return render(request, 'articles.html', context)