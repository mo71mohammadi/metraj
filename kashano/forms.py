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
    rooms = forms.CharField(label='rooms_count', max_length=100)
    floors = forms.CharField(label='floors_count', max_length=100)
    floor = forms.CharField(label='floor', max_length=100)
    flooring = forms.CharField(label='cover', max_length=100)
    view_material = forms.CharField(label='frontage', max_length=100)
    cabinet = forms.CharField(label='kitchen', max_length=100)
    sanad_stat = forms.CharField(label='document', max_length=100)
    fill_stat = forms.CharField(label='habitation', max_length=100)
    addr_latitude = forms.CharField(label='map_lat', max_length=100)
    addr_longitude = forms.CharField(label='map_long', max_length=100)
    eslahi = forms.CharField(label='has_modify', max_length=100)
    javaz_sakht = forms.CharField(label='has_manufacturing_license', max_length=100)
    ctime = forms.CharField(label='created_at', max_length=100)
    utime = forms.CharField(label='updated_at', max_length=100)

    class Meta:
        model = models.Estate
        # fields = '__all__'
        exclude = ['download_status', 'download_time', 'delete_status', 'name', 'owner_phone', 'owner_phone2']

    field_order = [
        "elead_id",
        "est_type",
        "area_id",
        "deal_type",
        "estate_id",
        "owner_name",
        "phone",
        "phone2",
        "est_address",
        "mortgage_only",
        "price",
        "mortgage_price",
        "price_rent",
        "dscr",
        "size_subs",
        "age",
        "rooms",
        "floors",
        "floor",
        "flooring",
        "view_material",
        "cabinet",
        "sanad_stat",
        "fill_stat",
        "addr_latitude",
        "addr_longitude",
        "eslahi",
        "javaz_sakht",
        "ctime",
        "utime"
    ]
