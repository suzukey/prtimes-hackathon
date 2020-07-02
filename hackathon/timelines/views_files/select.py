# -*- coding: utf-8 -*-

import json
import urllib.request

def company(co_id):

    url = "https://hackathon.stg-prtimes.net/company_release/"
    params = {
        'token': "e7zCG8N0sl5y"
    }

    i = 0
    page_num = 1
    body = []
    while(true):
        req = urllib.request.Request(
            '{}{}{}?{}'.format(url, co_id, page_num, urllib.parse.urlencode(params))
        )
            with urllib.request.urlopen(req) as res:
                body_temp = json.load(res)
        if body_temp["data"] == '':
            break
        else :
            for i in range(len(body_temp["data"]))
                rel_id[i] = body_temp["data"][i]["release_id"]

    return rel_id

def detail(co_id, cat_id):

    url = "https://hackathon.stg-prtimes.net/detail/"
    params = {
        'token': "e7zCG8N0sl5y"
    }

    i = 0
    body = []
    rel_id = company(co_id)
    while(rel_id != []):
        req = urllib.request.Request(
            '{}{}{}?{}'.format(url, co_id, rel_id[i], urllib.parse.urlencode(params))
        )
            with urllib.request.urlopen(req) as res:
                body_temp = json.load(res)
        if body_temp["data"] == '':
            break
        elif body_temp["main_category_id"] == cat_id :
            body[i] = {
            #'page': 1,                             #page number
            'data':[
                {
                    'company_id':   co_id,          #body_temp["company_id"]
                    'release_id':   rel_id[i],      #body_temp["release_id"]
                    'company_name':   body_temp["company_name"],
                    'title':   body_temp["title"],
                    'head':  body_temp["head"],     #リード文
                    'main_image':   body_temp["main_image"],
                    'created_at':   body_temp["created_at"],
                }
             ]
            }

            i += 1

    return body
