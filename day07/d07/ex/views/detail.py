from django.views.generic import DetailView
from django.views.generic import FormView
from ..models import Article
from ..forms import FavouriteForm

class Detail(DetailView, FormView):
    template_name = 'detail.html'
    model = Article
    form_class = FavouriteForm



