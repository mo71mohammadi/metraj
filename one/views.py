import json
import mysql
import pymongo
import requests
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.http import HttpResponse
from django.shortcuts import render, redirect

client = pymongo.MongoClient('localhost', 27017)
db = client['metrajDB']
col = db['kashano']
Setting = db['setting']


@staff_member_required()
@login_required()
def kashano(request):
    result = col.find({'est_type':'APARTMENT'}).limit(3000)
    records = []
    for object in result:
        records.append(object)
    paginator = Paginator(records, 100)
    records = paginator.get_page(request.GET.get('page'))
    notif = request.GET.get('page')

    return render(request, 'kashano.html', {'records':records, "notif": notif})


def notification(request):
    print(request.GET.get('page'))
    notif = request.GET.get('page')
    return render(request, 'kashano.html', {"notifi": notif})


def send(request):
    if request.GET.get('type') == 'kashano':
        data = col.find_one({"elead_id":int(request.GET.get('Value'))}, {'_id':0})
        print(data)
        data = json.dumps(data)
    else:
        data = "fail"
    mimetype = 'application/json'
    return HttpResponse(data, mimetype)


def get(request):
    if request.GET.get('refresh') == 'kashano':
        kashanoSet = Setting.find_one({"website":"kashano"}, {'_id':0})
        # dealType = ['EJARE', 'KHARID', 'PISHKHARID', 'MOAVEZE']
        # estType = ['APARTMENT', 'EDARI', 'MAGHAZE', 'VILA', 'KOLANGI', 'ZAMIN', 'BAAGH', 'BAAGHVILA']
        dealType = kashanoSet['transactions']
        estType = kashanoSet['estates']
        headers = {
            'Host':'www.kashano.ir',
            'User-Agent':'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:68.0) Gecko/20100101 Firefox/68.0',
            'Accept':'application/json, text/javascript, */*; q=0.01',
            'Accept-Language':'en-US,en;q=0.5',
            'Accept-Encoding':'gzip, deflate',
            'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8',
            'X-Requested-With':'XMLHttpRequest',
            'Content-Length':'16',
            'Connection':'keep-alive',
            # 'Cookie':'kashano=6c0d229bdca4dc1a9b0220c4431ace9a2d6e9fea; ksh_cache=4ziPvW1f17; _ga=GA1.2.971318184.1566732889; _gid=GA1.2.764954292.1566732889; username=; password=; _gat_UA-70446152-1=1',
            'Cookie':kashanoSet['cookie'],
        }
        for deal in dealType:
            for est in estType:
                data = {
                    'est_type':est,
                    'deal_type':deal,
                }
                levelOne = requests.post(url='http://www.kashano.ir/search', data=data, allow_redirects=True)
                breakNum = 0
                for page in range(1, 100000):
                    url = 'http://www.kashano.ir/search/listings/{}'.format(str(page))
                    data = {'sort_by':'ctime', 'sort_direction':'DESC', 'ctrl':'search'}
                    levelTwo = requests.post(url=url, data=data, cookies=levelOne.cookies)
                    if breakNum > 20:
                        break
                    print(page)
                    if levelTwo.json()['items']:
                        for ticket in levelTwo.json()['items']:
                            record = col.find_one({'elead_id':ticket['elead_id']})
                            if record:
                                breakNum += 1
                                # print(ticket['elead_id'])
                            else:
                                data = {'elead_id':ticket['elead_id']}
                                levelThree = requests.post(url='http://www.kashano.ir/est/owner_info', data=data,
                                                           headers=headers)
                                while not levelThree.text:
                                    levelThree = requests.post(url='http://www.kashano.ir/est/owner_info', data=data,
                                                               headers=headers)
                                print(est, deal, page)
                                dicDate = levelThree.json()
                                dicDate['elead_id'] = ticket['elead_id']
                                col.insert_one(dicDate)
                    else:
                        break

    return HttpResponse('بروز رسانی با موفقیت انجام شد!')


def setting(request):
    print(request.POST)
    result = Setting.find({}, {'_id':0})
    settings = []
    for setting in result:
        settings.append(setting)
    if request.POST.get('website') == 'kashano':
        update = {
            "cookie":request.POST.get('cookie'),
            "transactions":request.POST.getlist('transactions'),
            "estates":request.POST.getlist('estates'),
        }
        Setting.update_one({"website":"kashano"}, {"$set":update})
        return redirect('setting')

    return render(request, 'setting.html', {"settings":settings})
