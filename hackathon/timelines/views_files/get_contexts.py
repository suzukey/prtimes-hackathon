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

        data = detail(object.company_id)

        context = {
            'query': query_word,
            'data': data
        }

    return context


def get_timeline_context(request, company_id, release_id):
    context = {}

    data = get_objects(company_id, release_id)
    # data = com_objects(company_id, release_id)

    data = times_context(data)

    context['data'] = data

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


# 企業のプレスリリースリストすべて (未着手)
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


def times_context(no_time_data):
    data = []

    for ntd in no_time_data:
        year = str(ntd['created_at'])[:4]

        if year not in data:
            data.append({
                'year': year,
                'data': []
            })

        for ye_d in data:
            if year == ye_d['year']:
                ye_d['data'].append(ntd)

    return data


def get_com_name(company_id):
    url = "https://hackathon.stg-prtimes.net/company/"
    params = {
        'token': "e7zCG8N0sl5y"
    }
    request_url = '{}/{}'.format(
        url, company_id
    )

    res = requests.get(request_url, params=params)
    res_obj = json.loads(res.text)
    data = res_obj['data']['company_name']

    return data
