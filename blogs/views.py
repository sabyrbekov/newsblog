from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator
from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import redirect
from django.utils import timezone
from .models import Articles
from .forms import ArticleForm
from .utils import CategoryListViewMixin
from django.urls import reverse_lazy, reverse
from django.views.generic import (
                                ListView, CreateView, 
                                DetailView, UpdateView, 
                                DeleteView
                                )
"""
Вывод результатов поиска 
при помощи filter, models.Q
"""
class SearchResultsView(ListView):
    model = Articles
    template_name = 'blogs/search_results.html' 
    context_object_name = 'articles'

    def get_queryset(self):
        query = self.request.GET.get('search', '')
        if query:
            object_list = self.model.objects.filter(Q(title__icontains=query) | Q(content__icontains=query))
        else:
            object_list = self.model.objects.none()
        return object_list

"""
Вывод списка статей, 
где мы наследуемся от  ListView
"""
class ArticleListView(ListView):
    model = Articles
    template_name = 'blogs/article_list.html'
    context_object_name = 'articles'
    paginate_by = 3
    queryset = Articles.objects.all()


# class ArticleListView(ListView):
#     model = Articles
#     template_name = 'blogs/article_list.html'
#     context_object_name = 'articles'


# class KyrgyzstanArticleListView(CategoryListViewMixin):
#     model = Articles
#     template_name = 'blogs/article_list.html'
#     context_object_name = 'articles'
#     category_a = 'KG'

# class WorldArticleListView(CategoryListViewMixin):   
#     model = Articles
#     template_name = 'blogs/article_list.html'
#     context_object_name = 'articles'
#     category_a = 'WORLD'

# class SportArticleListView(CategoryListViewMixin):   
#     model = Articles
#     template_name = 'blogs/article_list.html'
#     context_object_name = 'articles'
#     category_a = 'SPORT'

"""
Вывод списка статей, 
где категория равняется "KG"
"""
class KyrgyzstanArticleListView(ListView):
    model = Articles
    template_name = 'blogs/article_list.html'
    context_object_name = 'articles'

    def get_queryset(self):
        objects_list = Articles.objects.filter(article_category='KG')
        return objects_list


"""
Вывод списка статей, 
где категория равняется "WORLD"
"""
class WorldArticleListView(ListView):
    model = Articles
    template_name = 'blogs/article_list.html'
    context_object_name = 'articles'

    def get_queryset(self):
        objects_list = Articles.objects.filter(article_category='WORLD')
        return objects_list


"""
Вывод списка статей, 
где категория равняется "SPORT"
"""
class SportArticleListView(ListView):
    model = Articles
    template_name = 'blogs/article_list.html'
    context_object_name = 'articles'

    def get_queryset(self):
        objects_list = Articles.objects.filter(article_category='SPORT')
        return objects_list

"""
Детальное рассмотрение статьи,
где мы наследуемся от DeleteView
"""

class ArticleDetailView(DeleteView):
    model = Articles
    template_name = 'blogs/article_detail.html'
    context_object_name = 'article'

"""
Создание статьи,
где мы наследуемся от CreateView
"""
class ArticleCreateView(CreateView):
    model = Articles
    template_name = 'blogs/article_create.html'
    fields = '__all__'
    success_url = reverse_lazy('articles_app:article_list')

"""
Обновление статьи, 
где мы наследуемся от UpdateView 
"""
class ArticleUpdateView(UpdateView):
    model = Articles
    template_name = 'blogs/article_update.html'
    fields = '__all__'
    
    def get_success_url(self):
        return reverse_lazy(
            'articles_app:article_detail',
            kwargs={'pk': self.object.pk},
        )

"""
Удаление статьи, 
где мы наследуемся от DeleteView 
"""
class ArticleDeleteView(DeleteView):
    model = Articles
    template_name = 'blogs/article_delete.html'
    success_url = reverse_lazy('articles_app:article_list')
