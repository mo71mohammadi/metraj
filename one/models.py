from django.db import models


class Equipment(models.Model):
    number = models.IntegerField(null=True, unique=True)
    title = models.CharField(max_length=100, null=True, blank=True)


class Estate(models.Model):
    equipments = models.ManyToManyField(Equipment)
    user_id = models.CharField(max_length=100, null=True, blank=True)
    data_id = models.IntegerField(null=True)
    estate_type_id = models.CharField(max_length=100, null=True, blank=True)
    installation = models.CharField(max_length=100, null=True, blank=True)
    name = models.CharField(max_length=100, null=True, blank=True)
    area = models.CharField(max_length=100, null=True, blank=True)
    land_area = models.CharField(max_length=100, null=True, blank=True)
    age = models.CharField(max_length=100, null=True, blank=True)
    front_length = models.CharField(max_length=100, null=True, blank=True)
    direction = models.CharField(max_length=100, null=True, blank=True)
    rooms_count = models.CharField(max_length=100, null=True, blank=True)
    floors_count = models.CharField(max_length=100, null=True, blank=True)
    units_count = models.CharField(max_length=100, null=True, blank=True)
    floor = models.CharField(max_length=100, null=True, blank=True)
    total_units_count = models.CharField(max_length=100, null=True, blank=True)
    cover = models.CharField(max_length=100, null=True, blank=True)
    frontage = models.CharField(max_length=100, null=True, blank=True)
    wc = models.CharField(max_length=100, null=True, blank=True)
    kitchen = models.CharField(max_length=100, null=True, blank=True)
    document = models.CharField(max_length=100, null=True, blank=True)
    has_building = models.CharField(max_length=100, null=True, blank=True)
    habitation = models.CharField(max_length=100, null=True, blank=True)
    address = models.CharField(max_length=500, null=True, blank=True)
    postal_code = models.CharField(max_length=100, null=True, blank=True)
    map = models.CharField(max_length=100, null=True, blank=True)
    mobile = models.CharField(max_length=100, null=True, blank=True)
    phone = models.CharField(max_length=100, null=True, blank=True)
    fronts_count = models.CharField(max_length=100, null=True, blank=True)
    lines_count = models.CharField(max_length=100, null=True, blank=True)
    has_modify = models.CharField(max_length=100, null=True, blank=True)
    allocation_type = models.CharField(max_length=100, null=True, blank=True)
    has_manufacturing_license = models.CharField(max_length=100, null=True, blank=True)
    has_wall = models.CharField(max_length=100, null=True, blank=True)
    has_landscaping = models.CharField(max_length=100, null=True, blank=True)
    vegetation = models.CharField(max_length=100, null=True, blank=True)
    car_way = models.CharField(max_length=100, null=True, blank=True)
    urban_position = models.CharField(max_length=100, null=True, blank=True)
    is_habitable = models.CharField(max_length=100, null=True, blank=True)
    has_agricultural_water = models.CharField(max_length=100, null=True, blank=True)
    has_endofwork = models.CharField(max_length=100, null=True, blank=True)
    distance_from_asphalt = models.CharField(max_length=100, null=True, blank=True)
    updated_by = models.CharField(max_length=100, null=True, blank=True)
    active = models.CharField(max_length=100, null=True, blank=True)
    created_at = models.CharField(max_length=100, null=True, blank=True)
    updated_at = models.CharField(max_length=100, null=True, blank=True)


class Advertisement(models.Model):
    estate = models.ForeignKey(Estate, null=True, on_delete=models.CASCADE)
    user_id = models.CharField(max_length=100, null=True, blank=True)
    agent_id = models.CharField(max_length=100, null=True, blank=True)
    transaction_type_id = models.CharField(max_length=100, null=True, blank=True)
    reject_id = models.CharField(max_length=100, null=True, blank=True)
    title = models.CharField(max_length=100, null=True, blank=True)
    slug = models.CharField(max_length=100, null=True, blank=True)
    settlement_sale_price = models.CharField(max_length=100, null=True, blank=True)
    sale_price = models.CharField(max_length=100, null=True, blank=True)
    settlement_rent_price = models.CharField(max_length=100, null=True, blank=True)
    mortgage_only = models.CharField(max_length=100, null=True, blank=True)
    mortgage_price = models.CharField(max_length=100, null=True, blank=True)
    rent_price = models.CharField(max_length=100, null=True, blank=True)
    sale_situation = models.CharField(max_length=100, null=True, blank=True)
    has_loan = models.CharField(max_length=100, null=True, blank=True)
    status = models.CharField(max_length=100, null=True, blank=True)
    is_special = models.CharField(max_length=100, null=True, blank=True)
    description = models.CharField(max_length=100, null=True, blank=True)
    expired_at = models.CharField(max_length=100, null=True, blank=True)
    updated_by = models.CharField(max_length=100, null=True, blank=True)
    visit = models.CharField(max_length=100, null=True, blank=True)
    active = models.CharField(max_length=100, null=True, blank=True)
    created_at = models.CharField(max_length=100, null=True, blank=True)
    updated_at = models.CharField(max_length=100, null=True, blank=True)


class Setting(models.Model):
    username = models.CharField(max_length=30, null=True, blank=True)
    password = models.CharField(max_length=30, null=True, blank=True)
    name = models.CharField(max_length=20, unique=True, null=True)
    cookie = models.CharField(max_length=500, null=True, blank=True)
    transactions = models.CharField(max_length=500, null=True, blank=True)
    estates = models.CharField(max_length=500, null=True, blank=True)


class EquipmentMetraj(models.Model):
    value = models.IntegerField(null=True)
    text = models.CharField(max_length=50, blank=True, null=True)


class EquipmentKashano(models.Model):
    metraj = models.ForeignKey(EquipmentMetraj, on_delete=models.CASCADE, null=True, blank=True)
    value = models.CharField(max_length=50, null=True)
    text = models.CharField(max_length=100, blank=True, null=True)


class AreaMetraj(models.Model):
    value = models.IntegerField(null=True)
    text = models.CharField(max_length=100, blank=True, null=True)


class AreaKashano(models.Model):
    metraj = models.ForeignKey(AreaMetraj, on_delete=models.CASCADE, null=True, blank=True)
    value = models.IntegerField(null=True)
    text = models.CharField(max_length=100, blank=True, null=True)


class DocumentMetraj(models.Model):
    value = models.IntegerField(null=True)
    text = models.CharField(max_length=100, blank=True, null=True)


class DocumentKashano(models.Model):
    metraj = models.ForeignKey(DocumentMetraj, on_delete=models.CASCADE, null=True)
    value = models.CharField(max_length=100, blank=True, null=True)
    text = models.CharField(max_length=100, blank=True, null=True)


class TransactionMetraj(models.Model):
    value = models.IntegerField(null=True)
    text = models.CharField(max_length=100, null=True)


class TransactionKashano(models.Model):
    metraj = models.ForeignKey(DocumentMetraj, on_delete=models.CASCADE, null=True)
    value = models.CharField(max_length=100, null=True)
    text = models.CharField(max_length=100, blank=True, null=True)


class HabitationMetraj(models.Model):
    value = models.IntegerField(null=True)
    text = models.CharField(max_length=100, null=True)


class HabitationKashano(models.Model):
    metraj = models.ForeignKey(HabitationMetraj, on_delete=models.CASCADE, null=True)
    value = models.CharField(max_length=100, null=True)
    text = models.CharField(max_length=100, blank=True, null=True)


class DirectionMetraj(models.Model):
    value = models.IntegerField(null=True)
    text = models.CharField(max_length=100, null=True)


class DirectionKashano(models.Model):
    metraj = models.ForeignKey(DirectionMetraj, on_delete=models.CASCADE, null=True)
    value = models.CharField(max_length=100, null=True)
    text = models.CharField(max_length=100, blank=True, null=True)


class EstateMetraj(models.Model):
    value = models.IntegerField(unique=True, null=True)
    text = models.CharField(max_length=100, null=True)


class EstateKashano(models.Model):
    metraj = models.ForeignKey(EstateMetraj, on_delete=models.CASCADE, null=True)
    value = models.CharField(max_length=100, null=True, unique=True)
    text = models.CharField(max_length=100, blank=True, null=True)
