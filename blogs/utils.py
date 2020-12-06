from django.shortcuts import render, get_object_or_404, redirect
from .models import Articles
from django.views.generic import ListView

class CategoryListViewMixin(ListView):
    model = None
    template_name = None


    def get_queryset(self):
        category_a = ''
        objects_ls = self.model.objects.filter(self.model.objects.article_category == category_a)
        return objects_ls


