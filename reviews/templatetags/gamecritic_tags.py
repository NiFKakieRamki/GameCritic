from django import template

register = template.Library()

@register.inclusion_tag('reviews/components/avatar.html')

def user_avatar(user):
    """
    UI-компонент 'Аватарка пользователя'.
    Принимает объект пользователя (User) и вычисляет инициал для отображения.
    """
    # Бизнес-логика компонента (безопасное извлечение первой буквы)
    if user and hasattr(user, 'username') and user.username:
        initial = user.username[0].upper()
    else:
        initial = "?"

    return {
        'user': user,
        'initial': initial
    }
