from django.urls import path
from . import views

app_name = 'reviews'

urlpatterns = [
    path('', views.review_list_view, name='list'),

    path('<slug:review_slug>/', views.review_detail_view, name='detail'),
]
