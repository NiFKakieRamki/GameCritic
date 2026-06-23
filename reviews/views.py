from django.shortcuts import render, get_object_or_404
from .models import Review

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