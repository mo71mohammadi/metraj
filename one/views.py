import ast
import json

import requests
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.http import HttpResponse
from django.shortcuts import render, redirect

from one import schema, models


@staff_member_required()
@login_required()
def kashano(request):
    records = models.Advertisement.objects.filter()
    paginator = Paginator(records, 1000)
    records = paginator.get_page(request.GET.get('page'))
    return render(request, 'kashano.html', {'records': records})


def send(request):
    if request.GET.get('type') == 'kashano':
        data = models.Advertisement.objects.get(id=int(request.GET.get('Value')))
        data = schema.JSON(data)
        data = json.dumps(data)
    else:
        data = "fail"
    mimetype = 'application/json'
    return HttpResponse(data, mimetype)


def get(request):
    if request.GET.get('refresh') == 'kashano':
        settings = models.Setting.objects.filter()
        for setting in settings:
            headers = {
                'Host': 'www.kashano.ir',
                'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:68.0) Gecko/20100101 Firefox/68.0',
                'Accept': 'application/json, text/javascript, */*; q=0.01',
                'Accept-Language': 'en-US,en;q=0.5',
                'Accept-Encoding': 'gzip, deflate',
                'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
                'X-Requested-With': 'XMLHttpRequest',
                'Content-Length': '16',
                'Connection': 'keep-alive',
                # 'Cookie':'kashano=6c0d229bdca4dc1a9b0220c4431ace9a2d6e9fea; ksh_cache=4ziPvW1f17; _ga=GA1.2.971318184.1566732889; _gid=GA1.2.764954292.1566732889; username=; password=; _gat_UA-70446152-1=1',
                'Cookie': setting.cookie,
            }

            for transaction in ast.literal_eval(setting.transactions):
                for estate in ast.literal_eval(setting.estates):
                    data = {
                        'est_type': estate,
                        'deal_type': transaction,
                    }
                    levelOne = requests.post(url='http://www.kashano.ir/search', data=data, allow_redirects=True)
                    print(transaction)
                    breakNum = 0
                    for page in range(1, 2):
                        url = 'http://www.kashano.ir/search/listings/{}'.format(str(page))
                        data = {'sort_by': 'ctime', 'sort_direction': 'DESC', 'ctrl': 'search'}
                        levelTwo = requests.post(url=url, data=data, cookies=levelOne.cookies)
                        if breakNum > 20:
                            break
                        print(transaction, page)

                        if levelTwo.json()['items']:
                            for ticket in levelTwo.json()['items']:
                                record = models.Estate.objects.filter(data_id=int(ticket['elead_id']))
                                if record:
                                    breakNum += 1
                                else:
                                    data = {'elead_id': ticket['elead_id']}
                                    levelThree = requests.post(url='http://www.kashano.ir/est/owner_info', data=data,
                                                               headers=headers)
                                    while not levelThree.text:
                                        levelThree = requests.post(url='http://www.kashano.ir/est/owner_info',
                                                                   data=data,
                                                                   headers=headers)
                                    print(transaction, estate, page)
                                    dicDate = levelThree.json()
                                    dicDate['elead_id'] = ticket['elead_id']
                                    schema.SQL(dicDate, action=1)
                        else:
                            break

    return HttpResponse('بروز رسانی با موفقیت انجام شد!')


def setting_get(request):
    settings = models.Setting.objects.filter(name="kashano")
    if request.POST.get('website') == 'kashano':
        if settings:
            settings.update(
                cookie=request.POST.get('cookie'), transactions=request.POST.getlist('transactions'),
                estates=request.POST.getlist('estates'), username=request.POST.get('username'),
                password=request.POST.get('password')
            )
        else:
            setting = models.Setting(
                cookie=request.POST.get('cookie'), transactions=request.POST.getlist('transactions'),
                estates=request.POST.getlist('estates'), name='kashano', username=request.POST.get('username'),
                password=request.POST.get('password')
            )
            setting.save()
        return redirect('setting_get')

    return render(request, 'setting_get.html', {"settings": settings})


def setting_metraj(request):
    typeDic = {
        'estates': models.EstateMetraj,
        'transactions': models.TransactionMetraj,
        'equipments': models.EquipmentMetraj,
        'areas': models.AreaMetraj,
        'documents': models.DocumentMetraj,
        'habitations': models.HabitationMetraj,
        'directions': models.DirectionMetraj,
    }

    if request.GET:
        request.session['type'] = request.GET.get('type')
    if request.POST:
        if request.POST.get('action') == 'delete':
            typeDic[request.session.get('type')].objects.filter(id=request.POST.get('item')).delete()
        if request.POST.get('action') == 'create':
            typeDic[request.session.get('type')](value=request.POST.get('value'), text=request.POST.get('text'))
        if request.POST.get('action') == 'update':
            typeDic[request.session.get('type')].objects.filter(id=request.POST.get('id')).update(
                value=request.POST.get('value'), text=request.POST.get('text'))
        if request.POST.get('action') == 'add':
            if not typeDic[request.session.get('type')].objects.filter(value=request.POST.get('value')):
                item = typeDic[request.session.get('type')](value=request.POST.get('value'),
                                                            text=request.POST.get('text'))
                item.save()
    content = {
        'items': typeDic[request.session.get('type')].objects.filter(),
        'type': request.session.get('type')
    }
    return render(request, 'setting_metraj.html', content)


def setting_kashano(request):
    typeDic = {
        'estates': models.EstateKashano,
        'transactions': models.TransactionKashano,
        'equipments': models.EquipmentKashano,
        'areas': models.AreaKashano,
        'documents': models.DocumentKashano,
        'habitations': models.HabitationKashano,
        'directions': models.DirectionKashano,
    }
    metraj = {
        'estates': models.EstateMetraj,
        'transactions': models.TransactionMetraj,
        'equipments': models.EquipmentMetraj,
        'areas': models.AreaMetraj,
        'documents': models.DocumentMetraj,
        'habitations': models.HabitationMetraj,
        'directions': models.DirectionMetraj,
    }

    if request.GET:
        request.session['type'] = request.GET.get('type')
    if request.POST:
        if request.POST.get('action') == 'delete':
            typeDic[request.session.get('type')].objects.filter(id=request.POST.get('item')).delete()
        if request.POST.get('action') == 'update':
            print(request.POST)
            typeDic[request.session.get('type')].objects.filter(id=request.POST.get('id')).update(
                value=request.POST.get('value'), text=request.POST.get('text'),
                metraj_id=int(request.POST.get('metraj')))
        if request.POST.get('action') == 'add':
            if not typeDic[request.session.get('type')].objects.filter(value=request.POST.get('value')):
                item = typeDic[request.session.get('type')](value=request.POST.get('value'),
                                                            metraj_id=int(request.POST.get('metraj')),
                                                            text=request.POST.get('text'))
                item.save()
    content = {
        'items': typeDic[request.session.get('type')].objects.filter(),
        'metrajs': metraj[request.session.get('type')].objects.filter(),
        'type': request.session.get('type')
    }
    return render(request, 'setting_kashano.html', content)
