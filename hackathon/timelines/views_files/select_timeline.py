import requests
import json


def company(co_id):

    url = "https://hackathon.stg-prtimes.net/company_release/"
    params = {
        'token': "e7zCG8N0sl5y"
    }

    page_num = 1
    body_temp = []
    rel_id = []
    while True:
        request_url = '{}/{}/{}'.format(url, co_id, page_num)

        res = requests.get(request_url, params=params)
        body_temp = json.loads(res.text)

        if len(body_temp["data"]) <= 0:
            break
        else:
            for i in range(len(body_temp["data"])):
                rel_id.append(body_temp["data"][i]["release_id"])

            page_num += 1

    return rel_id


def detail(co_id):

    url = "https://hackathon.stg-prtimes.net/detail/"
    params = {
        'token': "e7zCG8N0sl5y"
    }

    body = []
    rel_id = company(co_id)
    for i in range(len(rel_id)):
        request_url = '{}/{}/{}'.format(url, co_id, rel_id[i])

        res = requests.get(request_url, params=params)
        body_temp = json.loads(res.text)

        if 'title' in body_temp['data']:
            data = {
                'company_id': body_temp["company_id"],
                'release_id': body_temp["release_id"],
                'company_name': body_temp['data']["company_name"],
                'title': body_temp['data']["title"],
                'head': body_temp['data']["head"],  # リード文
                'main_image': body_temp['data']["main_image"],
                'created_at': body_temp['data']["created_at"],
            }
            body.append(data)

    return body
