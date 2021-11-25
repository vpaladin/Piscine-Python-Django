from django.views.generic import ListView
from ..models import Article

class Articles(ListView):
    model = Article
    template_name = 'articles.html'
    context_object_name = 'news'
    allow_empty = False
    # paginate_by = 50