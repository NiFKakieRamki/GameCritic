from django import forms
from .models import Review, Comment

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review #с какой моделью БД будет работать форма
        fields = ['title', 'content', 'cover_image', 'is_published'] #указываем какие поля разрешено менять пользователю

        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'text-slate-900 w-full px-4 py-3 rounded-xl border border-slate-300 focus:border-blue-500 focus:ring-2 focus:ring-blue-200 outline-none transition-all italic placeholder-slate-400',
                'placeholder': 'Например: За что мне полюбилась эта игра...'
            }),
            'content': forms.Textarea(attrs={
                'class': 'text-slate-900 w-full px-4 py-3 rounded-xl border border-slate-300 focus:border-blue-500 focus:ring-2 focus:ring-blue-200 outline-none transition-all min-h-[200px] italic placeholder-slate-400',
                'placeholder': 'Напишите текст вашей статьи здесь...'
            }),

            'cover_image': forms.ClearableFileInput(attrs={
                'class': 'block w-full text-sm text-slate-500 file:mr-4 file:py-2 file:px-4 file:rounded-xl file:border-0 file:text-sm file:font-semibold file:bg-blue-50 file:text-blue-700 hover:file:bg-blue-100 cursor-pointer',
                'id': 'image-upload-input'
            }),

            'is_published': forms.CheckboxInput(attrs={
                'class': 'w-5 h-5 text-blue-600 bg-gray-100 border-gray-300 rounded focus:ring-blue-500 cursor-pointer'

            })
        }

        labels = {
            'title': 'Заголовок публикации',
            'cover_image': 'Обложка обзора',
            'content': 'Текст публикации',
            'is_published': 'Опубликовать сразу?'
        }

class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ['body']
        widgets = {
        'body': forms.Textarea(attrs={
            'rows': 3,
            'class': 'w-full bg-white text-slate-900 px-4 py-3 rounded-xl border border-slate-300 placeholder-slate-400 resize-none focus:border-blue-500 focus:ring-2 focus:ring-blue-200 outline-none transition-all',
            'placeholder': 'Поделитесь мнением об этой игре...'
        })
    }

        labels = {
                'body': ''
            }