"""
 To render HTML pages
"""
from django.http import HttpResponse
from articles.models import Article
from random import randint
from django.template.loader import render_to_string
from django.contrib.auth.models import User

# def home(request):
#     random_num = randint(1, 3)
#     posts = Article.objects.get(id=random_num)
#     for post in posts:
#         p = post
#         HTML_STRING = f"""
#             <h1>{p.id} - {p.title}</h1>
#             <p>{p.content}</p>
#         """
        
#     p = posts
#     HTML_STRING = f"""
#         <h1>{p.id} - {p.title}</h1>
#         <a href="articles/{p.id}/">{p.content}</a>
#     """
    
#     return HttpResponse(HTML_STRING)

def home(request):    
    posts = Article.objects.all()
    context = {
        "articles": posts,
        "user": User
    }
    
    HTML_STRING = render_to_string("home-views.html", context)
    
    return HttpResponse(HTML_STRING)