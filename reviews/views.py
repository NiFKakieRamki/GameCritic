from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required 
from django.http import HttpResponseForbidden
from .models import Review
from .forms import ReviewForm, CommentForm

def review_list_view(request):
    reviews = Review.objects.filter(is_published=True).select_related('author')

    context = {
        'reviews': reviews,
    }

    return render(request, 'reviews/review_list.html', context)

def review_detail_view(request, review_slug):
    review = get_object_or_404(Review, slug=review_slug, is_published=True)
    comments = review.comments.all()

    if request.method == 'POST':
        if request.user.is_authenticated:
            form = CommentForm(request.POST)
            if form.is_valid():
                new_comment = form.save(commit=False)
                new_comment.review = review
                new_comment.author = request.user
                new_comment.save()

                return redirect('reviews:detail', review_slug=review.slug)
        else:
            return redirect('users:login')

    else:
        form = CommentForm()

    context = {
        'review': review,
        'comments': comments,
        'form': form  
    }

    return render(request, 'reviews/review_detail.html', context)

@login_required
def review_create_view(request):
    """
    Контроллер для создания новой публикации
    """
    #Если отправлена заполеннная форма
    if request.method == 'POST':
        form = ReviewForm(request.POST, request.FILES) # Передаем сырые данные

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

@login_required
def review_update_view(request, review_slug):
    review = get_object_or_404(Review, slug=review_slug)

    if review.author != request.user:
        return HttpResponseForbidden("Ошибка 403: Доступ запрещен.")

    if request.method == 'POST':
        form = ReviewForm(request.POST, request.FILES, instance=review)
        if form.is_valid():
            form.save() 
            return redirect('reviews:detail', review_slug=review.slug)
    else:
        form = ReviewForm(instance=review)

    return render(request, 'reviews/review_form.html', {'form': form, 'is_edit': True})

@login_required
def review_delete_view(request, review_slug):
    review = get_object_or_404(Review, slug=review_slug)

    if review.author != request.user:
        return HttpResponseForbidden("Ошибка 403: Доступ запрещен.")

    if request.method == 'POST':
        review.delete()
        return redirect('reviews:list')

    return render(request, 'reviews/review_confirm_delete.html', {'review': review})

@login_required
def like_toggle_view(request, review_slug):

    review = get_object_or_404(Review, slug=review_slug)

    if review.likes.filter(id=request.user.id).exists():
        review.likes.remove(request.user)
    else:
        review.likes.add(request.user)

    return redirect(request.META.get('HTTP_REFERER', 'reviews:list'))
