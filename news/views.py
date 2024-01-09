from django.shortcuts import render, get_object_or_404, redirect
from news.models import News, Category
from news.forms import CategoryForm

# Create your views here.


def home(request):
    context = {"all_news": News.objects.all()}
    return render(request, 'home.html', context)


def news_details(request, news_id):
    context = {"news": get_object_or_404(News, pk=news_id)}
    return render(request, 'news_details.html', context)


def categories_form(request):
    form = CategoryForm(request.POST or None)

    if form.is_valid():
        Category.objects.create(**form.cleaned_data)
        return redirect("home-page")

    return render(request, 'categories_form.html', {'form': form})
