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
