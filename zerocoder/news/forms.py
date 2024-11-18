from .models import NewsPost
from django.forms import ModelForm, TextInput, DateTimeInput, Textarea

class NewsPostForm(ModelForm):
    class Meta:
        model = NewsPost
        fields = ['title', 'shorts_description', 'text', 'pub_date']
        widgets = {
            'title': TextInput(attrs={'class' : 'form-control', 'placeholder': 'Введите заголовок новости'}),
            'shorts_description': TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите краткое описание'}),
            'text': Textarea(attrs={'class': 'form-control', 'placeholder': 'Введите текст новости'}),
            'pub_date': DateTimeInput(attrs={'class': 'form-control', 'placeholder': 'Дата публикации'})
        }

