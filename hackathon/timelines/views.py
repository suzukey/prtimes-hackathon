from django.shortcuts import render
from timelines.views_files.get_search_context import get_context


def search(request):
    template = 'companys/search.html'
    context = get_context(request)
    return render(request, template, context)


def timeline(request, company_id):
    template = 'timelines/index.html'
    context = {'data': ''}
    return render(request, template, context)
