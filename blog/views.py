from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Blog
from haystack.query import SearchQuerySet
import ast

# Create your views here.


class BlogPage(TemplateView):
    def get(self, request, **kwargs):
        return render(request, self.template_name, {})

    def post(self, request, **kwargs):
        query = request.POST.get('query', '')

        results = SearchQuerySet().models(Blog).filter(title=query)
        search_results = [result.title for result in results]

        search_details = ast.literal_eval(search_results[0])

        return render(request, self.template_name, {'search_details': search_details})
