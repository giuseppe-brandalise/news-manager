from django import forms
from news.models import User, Category, News


class CategoryForm(forms.Form):
    name = forms.CharField(
        label='Nome',
        max_length=200,
        widget=forms.TextInput(attrs=({'type': 'text'}))
        )


class NewsForm(forms.Form):
    title = forms.CharField(label='Título')
    content = forms.CharField(
        label='Conteúdo',
        widget=forms.Textarea
    )
    author = forms.ModelChoiceField(
        label='Autoria',
        queryset=User.objects.all()
    )
    created_at = forms.DateField(
        label='Criado em',
        widget=forms.DateInput(attrs={'type': 'date'})
    )
    image = forms.ImageField(label='URL da Imagem')
    categories = forms.ModelMultipleChoiceField(
        label='Categories',
        queryset=Category.objects.all(),
        widget=forms.CheckboxSelectMultiple
    )

    def save(self):
        news_data = self.cleaned_data
        new_news = News.objects.create(
            title=news_data['title'],
            content=news_data['content'],
            author=news_data['author'],
            created_at=news_data['created_at'],
            image=news_data['image'],
        )
        new_news.save()
