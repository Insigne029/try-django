from django.shortcuts import render
from .models import Article
from .forms import ArticleForm
from django.contrib.auth.decorators import login_required

# Create your views here.
def article_search_view(request):
    # print(request)
    # print(dir(request))
    # print(request.GET)
    query_dict= request.GET #this is a dictionary
    #query = query_dict.get("q") #<input type="text" name="q">
    try:
        query = int(query_dict.get("q"))
    except:
        query = None

    articles = None
    if query is not None:
        articles = Article.objects.get(id=query)
    context = {
        "article": articles
    }
    return render(request, "search.html", context)

def article_detail_view(request, pk=None):
    if pk is not None:
        articles = Article.objects.get(id=pk)
    
    context = {
        "article": articles
    }
    return render(request, "articles_detail.html", context)

@login_required
def article_create_view(request):
    form = ArticleForm(request.POST or None)
    # print(dir(form))
    context = {
        "form": form
    }
    
    if form.is_valid():
        article = form.save()
        context["form"] = ArticleForm()
        # title = form.cleaned_data.get("title")
        # content = form.cleaned_data.get("content")
        # article = Article.objects.create(title=title, content=content)
        # context["object"] = article
        # context["created"] = True
    
    return render(request, "create.html", context)