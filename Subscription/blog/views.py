from django.db.models import F
from django.views.generic import DetailView, CreateView

from blog.models import Article


class ArticleDetailView(DetailView):
    model = Article
    template_name = 'blog/article_detail.html'
    context_object_name = 'article'
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    pk_url_kwarg = 'pk'
    queryset = Article.objects.filter(status='p')

    def render_to_response(self, context, **response_kwargs):
        self.object.views = F('views') + 1
        self.object.save()
        response = super().render_to_response(context, **response_kwargs)
        return response


class ArticleCreateView(CreateView):
    ...
