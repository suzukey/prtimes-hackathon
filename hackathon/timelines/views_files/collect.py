# -*- coding: utf-8 -*-

# import select_timeline as sel
import spacy
# import pickle
nlp = spacy.load('ja_ginza')


def keywords(key_body):
    title = key_body["title"]
    title = title.replace('\n', '')
    head = key_body["head"]
    head = head.replace('\n', '')

    company = (
        'Company' or 'Position_Vocation' or 'Detective_Method_Other' or 'Product_Other' or 'Corporation_Other'
    )
    project = (
        'Product_Other' or 'Magagine' or 'Broadcast_Program' or 'Occation_Other' or 'Flora' or 'Person')

    prolist = []

    doc = nlp(title)

    for ent in doc.ents:
        if ent.label_ == project:
            prolist.append(ent.text)

    doc = nlp(head)
    for ent in doc.ents:
        if ent.label_ == project:
            prolist.append(ent.text)
        #print(ent.text, ent.start_char, ent.end_char, ent.label_)

    return prolist


def serch(key_body, body, prolist):
    timebody = []
    allpro = {}
    allcom = {}
    for j in range(len(prolist)):
        allpro[prolist[j]] = []

    for i in range(len(body)):
        title = body[i]["title"]
        title = title.replace('\n', '')
        head = body[i]["head"]
        head = head.replace('\n', '')

        company = (
            'Company' or 'Position_Vocation' or 'Detective_Method_Other' or 'Product_Other' or 'Corporation_Other')
        project = (
            'Product_Other' or 'Magagine' or 'Broadcast_Program' or 'Occation_Other' or 'Flora' or 'Person')

        doc = nlp(title)
        for ent in doc.ents:
            if ent.label_ == project:
                if ent.text in prolist:
                    allpro[ent.text].append(i)

        doc = nlp(head)
        for ent in doc.ents:
            if ent.label_ == project:
                if ent.text in prolist:
                    allpro[ent.text].append(i)

    list_1 = list(allpro.keys())  # 事業名の配列
    list_2 = list(allpro.values())  # 配列の配列
    list_3 = []
    l = len(list_2)
    for k in range(l-1):
        list_3[k] = len(list_2[k])
        list_2[k] = list(dict.fromkeys(list_2[k]))
     # 事業名 list_1[list_3.index(max)]
    if list_3 == []:
        tree = [key_body]
    else:
        for m in range(len(list_2(list_3.index(max(list_3, default=0))))):
            title = body[list_2[m]]["title"]
            title = title.replace('\n', '')
            head = body[list_2[m]]["head"]
            head = head.replace('\n', '')
            doc = nlp(title)
            for ent in doc.ents:
                if ent.label_ == company:
                    if ent.text in company:
                        allcom[ent.text].append(i)

            doc = nlp(head)
            for ent in doc.ents:
                if ent.label_ == company:
                    if ent.text in company:
                        allcom[ent.text].append(i)

        list_4 = list(allpro.keys())  # 企業名の配列
        list_5 = list(allpro.values())  # 配列の配列
        list_6 = []
        l = len(list_5)
        for k in range(l):
            list_6[k] = len(list_5[k])
            list_5[k] = list(dict.fromkeys(list_5[k]))
         # 企業名 list_4[list_6.index(max)]
        if list_6 == []:
            tree = [key_body]
        else:
            tree = []
            for n in range(len(list_5(list_6.index(max(list_6, default=0))))):
                data = {
                    # body_temp["company_id"]
                    'company_id':   body[list_2[n]]['company_id'],
                    # body_temp["release_id"]
                    'release_id':   body[list_2[n]]['release_id'],
                    'company_name':   body[list_2[n]]["company_name"],
                    'title':   body[list_2[n]]["title"],
                    'head':  body[list_2[n]]["head"],  # リード文
                    'main_image':   body[list_2[n]]["main_image"],
                    'created_at':   body[list_2[n]]["created_at"],
                    'project_name': list_1[list_3.index(max(list_3, default=0))],
                    'company_name': list_4[list_6.index(max(list_6, default=0))]
                }
                tree.apend(data)
    return tree
