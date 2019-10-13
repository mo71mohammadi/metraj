import csv
from functools import reduce
import operator
from django.db.models import Q
from django.shortcuts import render
import ast
import jdatetime
import requests
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.http import HttpResponse, HttpResponseNotFound, FileResponse
from django.shortcuts import render, redirect
from django.core import serializers
from kashano import models as model
import json
from . import forms
from openpyxl import Workbook


def change_date(time):
    time = time.split('-')
    time = jdatetime.date(int(time[0]), int(time[1]), int(time[2])).togregorian()
    return time


@staff_member_required()
@login_required()
def home(request):
    return render(request, 'blank.html')


@staff_member_required()
@login_required()
def get(request):
    settings = model.Setting.objects.filter()
    update_count = {}
    for setting in settings:
        Session = requests.session()
        Session.post('http://www.kashano.ir/user/login', data={'user': setting.username, 'pass': setting.password})
        for transaction in ast.literal_eval(setting.transactions):
            for estate in ast.literal_eval(setting.estates):
                item_count = 0
                filter_item = model.Estate.objects.filter(deal_type=transaction, est_type=estate)
                if filter_item:
                    max_date = filter_item.latest("ctime").ctime
                else:
                    max_date = jdatetime.date.today().togregorian() - jdatetime.timedelta(days=10)

                data = {'est_type': estate, 'deal_type': transaction}
                levelOne = Session.post(url='http://www.kashano.ir/search', data=data, allow_redirects=True)
                breakNum = 0
                for page in range(1, 5):
                    print(transaction, estate, page)
                    url = 'http://www.kashano.ir/search/listings/{}'.format(str(page))
                    data = {'sort_by': 'ctime', 'sort_direction': 'DESC', 'ctrl': 'search'}
                    levelTwo = Session.post(url=url, data=data, cookies=levelOne.cookies)
                    if levelTwo.json()['items']:
                        for ticket in levelTwo.json()['items']:
                            data = {'elead_id': ticket['elead_id']}
                            levelThree = Session.post(url='http://www.kashano.ir/est/owner_info', data=data)
                            while not levelThree.text:
                                levelThree = Session.post(url='http://www.kashano.ir/est/owner_info', data=data)
                            dic = levelThree.json()
                            new_time = change_date(dic['ctime'])
                            dic['ctime'] = new_time
                            dic['elead_id'] = ticket['elead_id']
                            if dic['ctime'] + jdatetime.timedelta(days=1) >= max_date:
                                print("true")
                                record = model.Estate.objects.filter(elead_id=ticket['elead_id'])
                                if record:
                                    print('record exist')
                                else:
                                    item_count += 1
                                    newEstate = model.Estate(
                                        elead_id=dic['elead_id'], name=dic['name'], phone=dic['phone'],
                                        phone2=dic['phone2'], est_address=dic['est_address'], est_id=dic['est_id'],
                                        user_id=dic['user_id'], owner_id=dic['owner_id'], owner_name=dic['owner_name'],
                                        owner_family=dic['owner_phone'], owner_phone2=dic['owner_phone2'],
                                        area_id=dic['area_id'],
                                        state_id=dic['state_id'], city_id=dic['city_id'], est_type=dic['est_type'],
                                        deal_type=dic['deal_type'], dependency=dic['dependency'],
                                        update_cap=dic['update_cap'],
                                        ctime=dic['ctime'], utime=dic['utime'], dealt_date=dic['dealt_date'],
                                        addr_area=dic['addr_area'],
                                        addr_generic=dic['addr_generic'], addr_private=dic['addr_private'],
                                        addr_plaq=dic['addr_plaq'], addr_unit_no=dic['addr_unit_no'],
                                        addr_map=dic['addr_map'], addr_latitude=dic['addr_latitude'],
                                        addr_longitude=dic['addr_longitude'], size_subs=dic['size_subs'],
                                        size=dic['size'], width=dic['width'],
                                        length=dic['length'], bar=dic['bar'],
                                        age=dic['age'], rooms=dic['rooms'], delete_status=False,
                                        floor=dic['floor'], floor_units=dic['floor_units'],
                                        floors=dic['floors'], phone_lines=dic['phone_lines'],
                                        view_material=dic['view_material'], cabinet=dic['cabinet'],
                                        price_meter=dic['price_meter'], price=dic['price'],
                                        price_rahnrent_val=dic['price_rahnrent_val'], price_rahn=dic['price_rahn'],
                                        price_rent=dic['price_rent'], rahnrent_exchange=dic['rahnrent_exchange'],
                                        fitfor=dic['fitfor'], fitfor_other=dic['fitfor_other'],
                                        eslahi=dic['eslahi'], tarakom=dic['tarakom'],
                                        arzegozar=dic['arzegozar'], ceil_height=dic['ceil_height'],
                                        wall_cover=dic['wall_cover'], hesar_type=dic['hesar_type'],
                                        trees_num=dic['trees_num'], trees_type=dic['trees_type'],
                                        trees_age=dic['trees_age'], water_share=dic['water_share'],
                                        sanad_stat=dic['sanad_stat'], fill_stat=dic['fill_stat'],
                                        stat=dic['stat'], tahvil_date=dic['tahvil_date'],
                                        viewable_owner_name=dic['viewable_owner_name'],
                                        dscr=dic['dscr'], javaz_sakht=dic['javaz_sakht'], pic_nums=dic['pic_nums'],
                                        default_pic=dic['default_pic'],
                                        is_updates=dic['is_updates'], edited_fields=dic['edited_fields'],
                                        water_share_amount=dic['water_share_amount'],
                                        water_share_unit=dic['water_share_unit'],
                                        water_share_inunit=dic['water_share_inunit'], pickup_num=dic['pickup_num'],
                                        is_hot=dic['is_hot'], old_price=dic['old_price'],
                                        old_price_meter=dic['old_price_meter'], old_price_rahn=dic['old_price_rahn'],
                                        old_price_rent=dic['old_price_rent'],
                                        old_price_rahnrent_val=dic['old_price_rahnrent_val'],
                                        update_user_id=dic['update_user_id'], old_ctime=dic['old_ctime'],
                                        area=dic['area'],
                                        old_price_dscr=dic['old_price_dscr'],
                                        old_price_meter_dscr=dic['old_price_meter_dscr'],
                                        old_price_rahn_dscr=dic['old_price_rahn_dscr'],
                                        old_price_rent_dscr=dic['old_price_rent_dscr'],
                                        old_price_rahnrent_val_dscr=dic['old_price_rahnrent_val_dscr']
                                    )
                                    newEstate.save()
                                    for item in dic['direction']:
                                        model.Direction(estate=newEstate, name=item).save()
                                    for item in dic['toilet']:
                                        model.Toilet(estate=newEstate, name=item).save()
                                    for item in dic['flooring']:
                                        model.Flooring(estate=newEstate, name=item).save()
                                    for item in dic['facilities']:
                                        model.Facilities(estate=newEstate, name=item).save()
                                    for item in dic['tasisat']:
                                        model.Tasisat(estate=newEstate, name=item).save()
                            else:
                                breakNum = 1
                    else:
                        break
                    if breakNum == 1:
                        break
                update_count[transaction + ' ' + estate] = item_count

    return HttpResponse(json.dumps(update_count), 'application/json')


@staff_member_required()
@login_required()
def get_setting(request):
    settings = model.Setting.objects.filter(name="kashano")
    if request.POST.get('website') == 'kashano':
        if settings:
            settings.update(
                cookie=request.POST.get('cookie'), transactions=request.POST.getlist('transactions'),
                estates=request.POST.getlist('estates'), username=request.POST.get('username'),
                password=request.POST.get('password')
            )
        else:
            setting = model.Setting(
                cookie=request.POST.get('cookie'), transactions=request.POST.getlist('transactions'),
                estates=request.POST.getlist('estates'), name='kashano', username=request.POST.get('username'),
                password=request.POST.get('password')
            )
            setting.save()
        return redirect('kashano_setting')

    return render(request, 'setting_get.html', {"settings": settings})


@staff_member_required()
@login_required()
def kashano(request):
    filter_names = ('download_status', 'deal_type', 'est_type', 'elead_id', 'name', 'area_id', 'delete_status')
    filter_clauses = [Q(**{filter: request.GET[filter]})
                      for filter in filter_names
                      if request.GET.get(filter)]
    if filter_clauses:
        print(filter_clauses)
        records = model.Estate.objects.filter(reduce(operator.and_, filter_clauses))
    else:
        records = model.Estate.objects.filter(delete_status=False)

    Session = requests.session()
    setting = model.Setting.objects.get(name='kashano')
    login = Session.post('http://www.kashano.ir/user/login', data={'user': setting.username, 'pass': setting.password})
    homes = Session.post(url='http://www.kashano.ir/pub/full_area_names', data={"city_id": "1"}, cookies=login.cookies)
    areas = []
    for item in homes.json():
        if not (item['area_id'] in areas):
            areas.append([item['area_id'], item['text']])
        if item['childs']:
            for result in item['childs']:
                if not (result['area_id'] in areas):
                    areas.append([result['area_id'], result['text']])
    paginator = Paginator(records, 300)
    records = paginator.get_page(request.GET.get('page'))
    return render(request, 'kashano.html', {'records': records, "areas": areas})


def obj_list(name):
    obj_list = []
    for obj in name:
        obj_list.append(obj.name)
    return obj_list


@staff_member_required()
@login_required()
def view_record(request):
    record = model.Estate.objects.filter(id=request.GET.get('id'))
    directions = model.Direction.objects.filter(estate_id=request.GET.get('id'))
    toilets = model.Toilet.objects.filter(estate_id=request.GET.get('id'))
    tasisats = model.Tasisat.objects.filter(estate_id=request.GET.get('id'))
    facilities = model.Facilities.objects.filter(estate_id=request.GET.get('id'))
    floorings = model.Flooring.objects.filter(estate_id=request.GET.get('id'))
    record_list = serializers.serialize('json', record)
    record_list = json.loads(record_list)
    record_list[0]['fields']['direction'] = obj_list(directions)
    record_list[0]['fields']['toilet'] = obj_list(toilets)
    record_list[0]['fields']['flooring'] = obj_list(floorings)
    record_list[0]['fields']['facilities'] = obj_list(facilities)
    record_list[0]['fields']['tasisat'] = obj_list(tasisats)
    record_list = json.dumps(record_list[0]['fields'])
    return HttpResponse(record_list, 'application/json')


@staff_member_required()
@login_required()
def edit_record(request):
    print(request.GET.get('id'))
    instance = model.Estate.objects.get(id=request.GET.get('id'))
    form = forms.EstateForm(instance=instance)
    if request.POST:
        form = forms.EstateForm(request.POST, instance=instance)
        if form.is_valid():
            print('as')
            form.save()
            return redirect("kashano")
        else:
            print(form.errors)

    return render(request, 'edit.html', {"form": form})


@staff_member_required()
@login_required()
def delete_record(request):
    print(request.GET.get('ids'))
    for item in request.GET.get('ids').split(','):
        print(item)
        model.Estate.objects.filter(id=item).update(delete_status=True)
    return redirect("kashano")


@staff_member_required()
@login_required()
def export_file(request):
    if request.GET.get('start'):
        start = request.GET.get('start')
    else:
        start = jdatetime.date.today().togregorian() - jdatetime.timedelta(days=2650)
    if request.GET.get('end'):
        end = request.GET.get('end')
    else:
        end = jdatetime.date.today().togregorian() + jdatetime.timedelta(days=10)
    filter_names = ('download_status', 'est_type', 'elead_id', 'name', 'area_id', 'delete_status')
    filter_clauses = [Q(**{filter: request.GET[filter]})
                      for filter in filter_names
                      if request.GET.get(filter)]
    filter_clauses.append(Q(ctime__range=[start, end]))
    record = model.Estate.objects.filter(reduce(operator.and_, filter_clauses))
    record_list = serializers.serialize('json', record)
    record_list = json.loads(record_list)

    new_list = []
    for item in record_list:
        directions = model.Direction.objects.filter(estate_id=item['pk'])
        toilets = model.Toilet.objects.filter(estate_id=item['pk'])
        tasisats = model.Tasisat.objects.filter(estate_id=item['pk'])
        facilities = model.Facilities.objects.filter(estate_id=item['pk'])
        floorings = model.Flooring.objects.filter(estate_id=item['pk'])
        item['fields']['direction'] = obj_list(directions)
        item['fields']['toilet'] = obj_list(toilets)
        item['fields']['flooring'] = obj_list(floorings)
        item['fields']['facilities'] = obj_list(facilities)
        item['fields']['tasisat'] = obj_list(tasisats)
        new_list.append(item['fields'])

    if request.GET.get('sort') == 'metraj':
        kashano_new_list = []
        for obj in new_list:
            newObj = {}
            newObj['estate_type_id'] = obj['est_type']
            del obj['est_type']
            newObj['region_id'] = obj['area_id']
            del obj['area_id']
            newObj['name'] = obj['owner_name']
            del obj['owner_name']
            newObj['area'] = obj['size_subs']
            del obj['size_subs']
            newObj['age'] = obj['age']
            del obj['age']
            newObj['direction'] = obj['direction']
            del obj['direction']
            newObj['rooms_count'] = obj['rooms']
            del obj['rooms']
            newObj['floors_count'] = obj['floors']
            del obj['floors']
            newObj['floor'] = obj['floor']
            del obj['floor']
            newObj['cover'] = obj['flooring']
            del obj['flooring']
            newObj['frontage'] = obj['view_material']
            del obj['view_material']
            newObj['wc'] = obj['toilet']
            del obj['toilet']
            newObj['document'] = obj['sanad_stat']
            del obj['sanad_stat']
            newObj['habitation'] = obj['fill_stat']
            del obj['fill_stat']
            newObj['address'] = obj['est_address']
            del obj['est_address']
            newObj['map'] = str(obj['addr_latitude']) + ', ' + str(obj['addr_longitude'])
            del obj['addr_latitude']
            del obj['addr_longitude']
            newObj['mobile'] = obj['phone']
            del obj['phone']
            newObj['phone'] = obj['phone2']
            del obj['phone2']
            newObj['has_modify'] = obj['eslahi']
            del obj['eslahi']
            newObj['has_manufacturing_license'] = obj['javaz_sakht']
            del obj['javaz_sakht']
            newObj['transaction_type_id'] = obj['deal_type']
            del obj['deal_type']
            newObj['sale_price'] = obj['price']
            del obj['price']
            newObj['mortgage_price'] = obj['price_rahn']
            del obj['price_rahn']
            newObj['rent_price'] = obj['price_rent']
            del obj['price_rent']
            newObj['description'] = obj['dscr']
            del obj['dscr']
            newObj['created_at'] = obj['ctime']
            del obj['ctime']
            newObj['updated_at'] = obj['utime']
            del obj['utime']
            newObj.update(obj)
            kashano_new_list.append(newObj)
        new_list = kashano_new_list

    if request.GET.get('format') == 'json':
        record_list = json.dumps(new_list)
        response = HttpResponse(record_list, content_type='application/json')
        response['Content-Disposition'] = 'attachment; filename=export.json'
    elif request.GET.get('format') == 'xlsx':
        wb = Workbook()
        ws = wb.active
        key_list = []
        if new_list:
            for key in new_list[0]:
                key_list.append(key)
        ws.append(key_list)
        for record in new_list:
            new_values = []
            for item in list(record.values()):
                if type(item) == list:
                    new_values.append(', '.join(item))
                else:
                    new_values.append(str(item))
            ws.append(new_values)
        wb.save('export.xlsx')
        response = FileResponse(open('export.xlsx', 'rb'))
        response['Content-Disposition'] = 'attachment; filename="export.xlsx"'
    else:
        response = HttpResponse('Parameter Format Not Correct')
    return response
