import requests
import json
from django.db.models import Q

from companys.models import Company
from timelines.views_files.select_timeline import detail
from timelines.views_files.collect import keywords, search_relase


def get_search_context(request):
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


def get_timeline_context(request, company_id, release_id):
    context = {}

    context['data'] = get_objects(company_id, release_id)
    # context['data'] = com_objects(company_id, release_id)

    return context


# 事業のプレスリリースタイムライン
def get_objects(company_id, release_id):
    url = "https://hackathon.stg-prtimes.net/detail/"
    params = {
        'token': "e7zCG8N0sl5y"
    }
    request_url = '{}/{}/{}'.format(
        url, company_id, release_id
    )

    res = requests.get(request_url, params=params)
    res_obj = json.loads(res.text)

    pre = res_obj['data']
    keywd = keywords(pre)

    details = detail(company_id)
    data = search_relase(res_obj['data'], details, keywd)

    return data


# 企業のプレスリリースリストすべて
def com_objects(company_id, release_id):
    url = "https://hackathon.stg-prtimes.net/detail/"
    params = {
        'token': "e7zCG8N0sl5y"
    }
    request_url = '{}/{}/{}'.format(
        url, company_id, release_id
    )

    res = requests.get(request_url, params=params)
    res_obj = json.loads(res.text)
    data = res_obj['data']

    return data
