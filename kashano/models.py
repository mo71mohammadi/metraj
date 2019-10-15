from django.db import models


class Estate(models.Model):
    estate_type_id = models.CharField(max_length=50, null=True, blank=True)
    region_id = models.CharField(max_length=50, null=True, blank=True)
    transaction_type_id = models.CharField(max_length=50, null=True, blank=True)
    estate_id = models.CharField(max_length=50, null=True, blank=True, unique=True)
    owner_name = models.CharField(max_length=50, null=True, blank=True)
    mobile = models.CharField(max_length=50, null=True, blank=True)
    phone = models.CharField(max_length=50, null=True, blank=True)
    address = models.CharField(max_length=300, null=True, blank=True)
    sale_price = models.CharField(max_length=50, null=True, blank=True)
    mortgage_price = models.CharField(max_length=50, null=True, blank=True)
    rent_price = models.CharField(max_length=50, null=True, blank=True)
    description = models.CharField(max_length=300, null=True, blank=True)
    area = models.CharField(max_length=50, null=True, blank=True)
    age = models.CharField(max_length=50, null=True, blank=True)
    rooms_count = models.CharField(max_length=50, null=True, blank=True)
    floors_count = models.CharField(max_length=50, null=True, blank=True)
    floor = models.CharField(max_length=50, null=True, blank=True)
    frontage = models.CharField(max_length=50, null=True, blank=True)
    kitchen = models.CharField(max_length=50, null=True, blank=True)
    document = models.CharField(max_length=50, null=True, blank=True)
    habitation = models.CharField(max_length=50, null=True, blank=True)
    map = models.CharField(max_length=100, null=True, blank=True)
    has_modify = models.CharField(max_length=50, null=True, blank=True)
    has_manufacturing_license = models.CharField(max_length=50, null=True, blank=True)
    created_at = models.DateField(null=True, blank=True)
    updated_at = models.CharField(max_length=50, null=True, blank=True)

    area_kashano = models.CharField(max_length=50, null=True, blank=True)
    download_status = models.BooleanField(default=False, null=True, blank=True)
    delete_status = models.BooleanField(default=False, null=True, blank=True)
    name = models.CharField(max_length=50, null=True, blank=True)
    est_id = models.CharField(max_length=50, null=True, blank=True)
    user_id = models.CharField(max_length=50, null=True, blank=True)
    owner_id = models.CharField(max_length=50, null=True, blank=True)
    owner_family = models.CharField(max_length=50, null=True, blank=True)
    owner_phone = models.CharField(max_length=50, null=True, blank=True)
    owner_phone2 = models.CharField(max_length=50, null=True, blank=True)
    state_id = models.CharField(max_length=50, null=True, blank=True)
    city_id = models.CharField(max_length=50, null=True, blank=True)
    dependency = models.CharField(max_length=50, null=True, blank=True)
    update_cap = models.CharField(max_length=50, null=True, blank=True)
    dealt_date = models.CharField(max_length=50, null=True, blank=True)
    addr_area = models.CharField(max_length=300, null=True, blank=True)
    addr_generic = models.CharField(max_length=300, null=True, blank=True)
    addr_private = models.CharField(max_length=300, null=True, blank=True)
    addr_plaq = models.CharField(max_length=50, null=True, blank=True)
    addr_unit_no = models.CharField(max_length=50, null=True, blank=True)
    addr_map = models.CharField(max_length=50, null=True, blank=True)
    size = models.CharField(max_length=50, null=True, blank=True)
    width = models.CharField(max_length=50, null=True, blank=True)
    length = models.CharField(max_length=50, null=True, blank=True)
    bar = models.CharField(max_length=50, null=True, blank=True)
    floor_units = models.CharField(max_length=50, null=True, blank=True)
    phone_lines = models.CharField(max_length=50, null=True, blank=True)
    other_facilities = models.CharField(max_length=50, null=True, blank=True)
    price_meter = models.CharField(max_length=50, null=True, blank=True)
    price_rahnrent_val = models.CharField(max_length=50, null=True, blank=True)
    rahnrent_exchange = models.CharField(max_length=50, null=True, blank=True)
    fitfor = models.CharField(max_length=50, null=True, blank=True)
    fitfor_other = models.CharField(max_length=50, null=True, blank=True)
    tarakom = models.CharField(max_length=50, null=True, blank=True)
    arzegozar = models.CharField(max_length=50, null=True, blank=True)
    ceil_height = models.CharField(max_length=50, null=True, blank=True)
    wall_cover = models.CharField(max_length=50, null=True, blank=True)
    hesar_type = models.CharField(max_length=50, null=True, blank=True)
    trees_num = models.CharField(max_length=50, null=True, blank=True)
    trees_type = models.CharField(max_length=50, null=True, blank=True)
    trees_age = models.CharField(max_length=50, null=True, blank=True)
    water_share = models.CharField(max_length=50, null=True, blank=True)
    stat = models.CharField(max_length=50, null=True, blank=True)
    tahvil_date = models.CharField(max_length=50, null=True, blank=True)
    viewable_owner_name = models.CharField(max_length=50, null=True, blank=True)
    pic_nums = models.CharField(max_length=50, null=True, blank=True)
    default_pic = models.CharField(max_length=50, null=True, blank=True)
    is_updates = models.CharField(max_length=50, null=True, blank=True)
    edited_fields = models.CharField(max_length=50, null=True, blank=True)
    water_share_amount = models.CharField(max_length=50, null=True, blank=True)
    water_share_unit = models.CharField(max_length=50, null=True, blank=True)
    water_share_inunit = models.CharField(max_length=50, null=True, blank=True)
    pickup_num = models.CharField(max_length=50, null=True, blank=True)
    is_hot = models.CharField(max_length=50, null=True, blank=True)
    old_price = models.CharField(max_length=50, null=True, blank=True)
    old_price_meter = models.CharField(max_length=50, null=True, blank=True)
    old_price_rahn = models.CharField(max_length=50, null=True, blank=True)
    old_price_rent = models.CharField(max_length=50, null=True, blank=True)
    old_price_rahnrent_val = models.CharField(max_length=50, null=True, blank=True)
    update_user_id = models.CharField(max_length=50, null=True, blank=True)
    old_ctime = models.CharField(max_length=50, null=True, blank=True)
    area = models.CharField(max_length=300, null=True, blank=True)
    old_price_dscr = models.CharField(max_length=50, null=True, blank=True)
    old_price_meter_dscr = models.CharField(max_length=50, null=True, blank=True)
    old_price_rahn_dscr = models.CharField(max_length=50, null=True, blank=True)
    old_price_rent_dscr = models.CharField(max_length=50, null=True, blank=True)
    old_price_rahnrent_val_dscr = models.CharField(max_length=50, null=True, blank=True)


class Direction(models.Model):
    estate = models.ForeignKey(Estate, on_delete=models.CASCADE)
    name = models.CharField(max_length=50, null=True, blank=True)


class Toilet(models.Model):
    estate = models.ForeignKey(Estate, on_delete=models.CASCADE)
    name = models.CharField(max_length=50, null=True, blank=True)


class Flooring(models.Model):
    estate = models.ForeignKey(Estate, on_delete=models.CASCADE)
    name = models.CharField(max_length=50, null=True, blank=True)


class Facilities(models.Model):
    estate = models.ForeignKey(Estate, on_delete=models.CASCADE)
    name = models.CharField(max_length=50, null=True, blank=True)


class Tasisat(models.Model):
    estate = models.ForeignKey(Estate, on_delete=models.CASCADE)
    name = models.CharField(max_length=50, null=True, blank=True)


class Setting(models.Model):
    username = models.CharField(max_length=30, null=True, blank=True)
    password = models.CharField(max_length=30, null=True, blank=True)
    name = models.CharField(max_length=20, unique=True, null=True)
    cookie = models.CharField(max_length=500, null=True, blank=True)
    transactions = models.CharField(max_length=500, null=True, blank=True)
    estates = models.CharField(max_length=500, null=True, blank=True)


class Area(models.Model):
    area_id = models.CharField(unique=True, max_length=30, blank=True, null=True)
    text = models.CharField(max_length=300, blank=True, null=True)
