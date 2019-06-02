from django.urls import re_path
from . import views

urlpatterns = [
    re_path(r'^blog-search/', views.BlogPage.as_view(template_name='blog_search.html'), name='blog-search'),
]

