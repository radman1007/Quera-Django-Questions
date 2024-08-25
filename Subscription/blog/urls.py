from django.urls import path

from .views import ArticleDetailView, ArticleCreateView

app_name = 'blog'
urlpatterns = [
    path('create-article/', ArticleCreateView.as_view(), name="create"),
    path('article/<slug:slug>/', ArticleDetailView.as_view(), name="detail"),
]
