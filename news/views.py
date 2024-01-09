from django.shortcuts import render, get_object_or_404
from news.models import News

# Create your views here.


def home(request):
    context = {"all_news": News.objects.all()}
    return render(request, 'home.html', context)


def news_details(request, news_id):
    context = {"news": get_object_or_404(News, pk=news_id)}
    return render(request, 'news_details.html', context)
