from django.shortcuts import render
from news.models import News

# Create your views here.


def home(request):
    context = {"all_news": News.objects.all()}
    return render(request, 'home.html', context)
