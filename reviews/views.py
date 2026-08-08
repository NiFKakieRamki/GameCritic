from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required #Защита маршрута
from .models import Review
from .forms import ReviewForm

def review_list_view(request):
    reviews = Review.objects.filter(is_published=True).select_related('author')

    context = {
        'reviews': reviews,
    }

    return render(request, 'reviews/review_list.html', context)

def review_detail_view(request, review_slug):
    review = get_object_or_404(Review, slug=review_slug, is_published=True)

    context = {
        'review': review
    }

    return render(request, 'reviews/review_detail.html', context)

@login_required
def review_create_view(request):
    """
    Контроллер для создания новой публикации
    """
    #Если отправлена заполеннная форма
    if request.method == 'POST':
        form = ReviewForm(request.POST) # Передаем сырые данные

        # Запускаем валидацию
        if form.is_valid():

            #Так как в форме нет автора, то сохраняем пока только в памяти без коммита в БД
            new_review = form.save(commit=False) 

            new_review.author = request.user # теперь назначили авторизированного пользователя посту

            new_review.save() # и теперь все сохраняем в БД


            # успешный POST завершается редиректом
            return redirect('reviews:detail', review_slug=new_review.slug)

    else:
        form = ReviewForm() # если GET, то даем пустую форму

    context = {
            'form': form
        }
    return render(request, 'reviews/review_form.html', context)

