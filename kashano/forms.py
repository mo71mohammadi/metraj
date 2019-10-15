from django import forms
from . import models


class EstateForm(forms.ModelForm):
    elead_id = forms.CharField(label='id', max_length=100)
    est_type = forms.CharField(label='estate_type_id', max_length=100)
    area_id = forms.CharField(label='region_id', max_length=100)
    deal_type = forms.CharField(label='transaction_type_id', max_length=100)
    estate_id = forms.CharField(label='estate_id', max_length=100)
    owner_name = forms.CharField(label='name', max_length=100)
    phone = forms.CharField(label='mobile', max_length=100)
    phone2 = forms.CharField(label='phone', max_length=100)
    est_address = forms.CharField(label='address', max_length=100)
    mortgage_only = forms.CharField(label='mortgage_only', max_length=100)
    price = forms.CharField(label='sale_price', max_length=100)
    mortgage_price = forms.CharField(label='mortgage_price', max_length=100)
    price_rent = forms.CharField(label='rent_price', max_length=100)
    dscr = forms.CharField(label='description', max_length=100)
    size_subs = forms.CharField(label='area', max_length=100)
    age = forms.CharField(label='age', max_length=100)
    front_length = forms.CharField(label='front_length', max_length=100)

    class Meta:
        model = models.Estate
        # fields = '__all__'
        exclude = ['download_status', 'download_time', 'delete_status', 'name', 'owner_phone', 'owner_phone2']
    field_order = ['elead_id', 'est_type', 'area_id']

def change_data(new_list):
    kashano_new_list = []
    for obj in new_list:
        newObj = {}
        newObj['id'] = obj['id']
        newObj['estate_type_id'] = obj['est_type']
        del obj['est_type']
        newObj['region_id'] = obj['area_id']
        del obj['area_id']
        newObj['transaction_type_id'] = obj['deal_type']
        del obj['deal_type']
        newObj['estate_id'] = obj['elead_id']
        del obj['elead_id']
        newObj['name'] = obj['name']
        del obj['owner_name']
        del obj['name']
        if not obj['phone2']:
            obj['phone2'] = ''
        Phone = re.search(r'''^[9]\d{9}|^[0]\d{10}''', obj['phone'])
        Phone2 = re.search(r'''^[9]\d{9}|^[0]\d{10}''', obj['phone2'])
        if Phone:
            newObj['mobile'] = Phone[0]
            newObj['phone'] = obj['phone2']
        elif Phone2:
            newObj['mobile'] = Phone2[0]
            newObj['phone'] = obj['phone']
        else:
            newObj['mobile'] = ''
            newObj['phone'] = ''
        del obj['phone']
        del obj['phone2']
        del obj['owner_phone']
        del obj['owner_phone2']
        newObj['address'] = obj['est_address']
        del obj['est_address']
        newObj['sale_price'] = obj['price']
        del obj['price']
        newObj['mortgage_price'] = obj['price_rahn']
        del obj['price_rahn']
        newObj['rent_price'] = obj['price_rent']
        del obj['price_rent']
        newObj['description'] = obj['dscr']
        del obj['dscr']
        newObj['area'] = obj['size_subs']
        del obj['size_subs']
        newObj['age'] = obj['age']
        del obj['age']
        newObj['front_length'] = ''
        newObj['direction'] = obj['direction']
        del obj['direction']
        newObj['rooms_count'] = obj['rooms']
        del obj['rooms']
        newObj['floors_count'] = obj['floors']
        del obj['floors']
        newObj['units_count'] = ''
        newObj['floor'] = obj['floor']
        del obj['floor']
        newObj['total_units_count'] = ''
        newObj['cover'] = obj['flooring']
        del obj['flooring']
        newObj['frontage'] = obj['view_material']
        del obj['view_material']
        newObj['wc'] = obj['toilet']
        del obj['toilet']
        newObj['kitchen'] = obj['cabinet']
        del obj['cabinet']
        newObj['document'] = obj['sanad_stat']
        del obj['sanad_stat']
        newObj['habitation'] = obj['fill_stat']
        del obj['fill_stat']
        newObj['map'] = str(obj['addr_latitude']) + ', ' + str(obj['addr_longitude'])
        del obj['addr_latitude']
        del obj['addr_longitude']
        newObj['has_modify'] = obj['eslahi']
        del obj['eslahi']
        newObj['has_manufacturing_license'] = obj['javaz_sakht']
        del obj['javaz_sakht']
        newObj['urban_position'] = ''
        newObj['has_endofwork'] = ''
        newObj['created_at'] = obj['ctime']
        del obj['ctime']
        newObj['updated_at'] = obj['utime']
        del obj['utime']
        newObj['area_kashano'] = obj['area']
        del obj['area']

        newObj.update(obj)
        kashano_new_list.append(newObj)
    return kashano_new_list

