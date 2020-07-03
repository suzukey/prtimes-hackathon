from django.shortcuts import render
from timelines.views_files.get_contexts import get_search_context, get_timeline_context


def index(request):
    template = 'index.html'
    context = {}
    return render(request, template, context)


def search(request):
    template = 'companys/search.html'
    context = get_search_context(request)
    return render(request, template, context)


def timeline(request, company_id, release_id):
    template = 'timelines/index.html'
    context = get_timeline_context(request, company_id, release_id)
    return render(request, template, context)


def more(request, company_id, release_id, year):
    template = 'timelines/more.html'
    context = get_timeline_context(request, company_id, release_id)
    return render(request, template, context)
