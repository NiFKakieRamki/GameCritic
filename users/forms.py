from django import forms
from django.contrib.auth import get_user_model
from .models import Profile

User = get_user_model()

# заготовка для виджетов
INPUT_CLASSES = ('w-full bg-gc-bg border border-gc-border rounded-xl px-4 py-3 text-white text-sm placeholder-zinc-500 focus:outline-none focus:border-gc-accent transition-all')

class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email']
        widgets = {
            'username': forms.TextInput(attrs={
                'class': INPUT_CLASSES,
                'placeholder': 'Ваш никнейм'
            }),
            'email': forms.EmailInput(attrs={
                'class': INPUT_CLASSES,
                'placeholder': 'Ваша почта'
            }),
        }

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['avatar', 'bio']
        widgets = {
            'avatar': forms.ClearableFileInput(attrs={
                'class':'block w-full text-xs text-zinc-400 file:mr-4 file:py-2.5 file:px-4 file:rounded-xl file:border-0 file:text-xs file:font-bold file:bg-gc-accent/20 file:text-white file:cursor-pointer transition-colors'
            }),
            'bio': forms.Textarea(attrs={
                'class': INPUT_CLASSES
            }),
        }

    