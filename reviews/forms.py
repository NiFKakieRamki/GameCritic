from django import forms
from .models import Review

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review #с какой моделью БД будет работать форма
        fields = ['title', 'content', 'is_published'] #указываем какие поля разрешено менять пользователю

        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'text-slate-900 w-full px-4 py-3 rounded-xl border border-slate-300 focus:border-blue-500 focus:ring-2 focus:ring-blue-200 outline-none transition-all italic placeholder-slate-400',
                'placeholder': 'Например: За что мне полюбилась эта игра...'
            }),
            'content': forms.Textarea(attrs={
                'class': 'text-slate-900 w-full px-4 py-3 rounded-xl border border-slate-300 focus:border-blue-500 focus:ring-2 focus:ring-blue-200 outline-none transition-all min-h-[200px] italic placeholder-slate-400',
                'placeholder': 'Напишите текст вашей статьи здесь...'
            }),
            'is_published': forms.CheckboxInput(attrs={
                'class': 'w-5 h-5 text-blue-600 bg-gray-100 border-gray-300 rounded focus:ring-blue-500 cursor-pointer'

            })
        }

        labels = {
            'title': 'Заголовок публикации',
            'content': 'Текст публикации',
            'is_published': 'Опубликовать сразу?'
        }

