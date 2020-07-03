from django.db.models import Q

from companys.models import Company
from timelines.views_files.select_timeline import detail


def get_context(request):
    context = {}

    if 'q' in request.GET:
        query_word = request.GET.get('q')
        object = Company.objects.filter(
            Q(company_name__icontains=query_word)
        ).first()

        context = {
            'query': query_word,
            'data': detail(object.company_id)
        }

    return context
