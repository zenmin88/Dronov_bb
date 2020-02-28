from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy, reverse

from .models import Bb, Category
from .forms import BbForm


class BbCreateView(CreateView):
    template_name = 'bboard/create.html'
    form_class = BbForm
    success_url = reverse_lazy('index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        return context


def index(request):
    objects = Bb.objects.all()
    category = Category.objects.all()
    context = {'bbs': objects, 'category': category}
    return render(request, 'bboard/index.html', context)


def category_view(request, category_id):
    bbs = Bb.objects.filter(category=category_id)
    categories = Category.objects.all()
    current_category = Category.objects.get(pk=category_id)
    context = {
        'bbs': bbs,
        'categories': categories,
        'current_category': current_category
    }
    return render(request, 'bboard/category_view.html', context)





