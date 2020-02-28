from django.urls import path

from .views import index, category_view, BbCreateView

urlpatterns = [
    path('', index, name='index'),
    path('<int:category_id>', category_view, name='category_view'),
    path('add/', BbCreateView.as_view(), name='add'),
]