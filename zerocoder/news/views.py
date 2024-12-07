from django.shortcuts import render, redirect
from .models import NewsPost
from .forms import NewsPostForm

def home(request):
    news = NewsPost.objects.all()
    return render(request, 'news/news.html', {'news' : news})

def create_news(request):
    error = ''
    if request.method == 'POST':
        form = NewsPostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('news_home')
        else:
            errors = 'Данные были заполнены некорректно'
    form = NewsPostForm()
    return render(request, 'news/add_new_post.html', {'form' : form, 'errors' : error})