from django.shortcuts import render, get_object_or_404
from .models import Article
from django.http import JsonResponse
from django.forms.models import model_to_dict
from django.db.models import Q
from django.views import View
def article_list(request):
    articles =[model_to_dict(i) for i in  Article.objects.all()]
    return JsonResponse({'articles': articles})

def article_detail(request, article_id):
    article = model_to_dict(get_object_or_404(Article, pk=article_id))
    return JsonResponse({'article': article})
class ArticleSearchView(View):
    def get(self, request):
        query = request.GET.get('query')
        articles = Article.objects.filter(Q(title__icontains=query))
        data = [{'id':article.id,'title': article.title, 'source': article.source, 'date': article.date, 'content': article.content} for article in articles]
        return JsonResponse({'articles':data})

def index(request):
    return render(request, 'index.html')
def detail(request):
    return render(request, 'detail.html')
def search(request):
    return render(request, 'search.html')
def about(request):
    return render(request, 'about.html')
def contact(request):
    return render(request, 'contact.html')