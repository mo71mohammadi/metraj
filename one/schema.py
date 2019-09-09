import re

from one import models


def SQL(record, action):
    estTypeL = [
        ('MAGHAZE', 1), ('EDARI', 2), ('ZAMIN', 3), ('KOLANGI', 4), ('VILA', 5), ('BAAGHVILA', 5), ('APARTMENT', 6),
        ('BAAGH', 8)
    ]
    estType = None
    for est in estTypeL:
        if est[0] == record['est_type']:
            estType = est[1]

    rePhone = re.search(r'''^[9]\d{9}|^[0]\d{10}''', record['phone'])
    rePhone2 = re.search(r'''^[9]\d{9}|^[0]\d{10}''', record['phone2'])
    if rePhone:
        mobile = rePhone[0]
        phone = record['phone2']
    elif rePhone2:
        mobile = rePhone2[0]
        phone = record['phone2']
    else:
        mobile = ''
        phone = ''

    if record['age']:
        age = int(record['age'])
    else:
        age = ''

    if record['addr_latitude'] and record['addr_longitude']:
        map = record['addr_latitude'] + ', ' + record['addr_longitude']
    else:
        map = ''

    directionL = []
    for direct in record['direction']:
        if direct == 'SHOMALI':
            directionL.append(1)
        elif direct == 'SHARGHI':
            directionL.append(2)
        elif direct == 'JONOOBI':
            directionL.append(3)
        elif direct == 'GHARBI':
            directionL.append(4)
    if record['fill_stat'] == 'TAKHLIE':
        habitation = 0
    elif record['fill_stat'] == 'MALEKSAKEN':
        habitation = 1
    elif record['fill_stat'] == 'EJARE':
        habitation = 2
    else:
        habitation = ''

    if record['sanad_stat'] == 'SHAKHSI':
        document = 2
    elif record['sanad_stat'] == 'TEJARI':
        document = 3
    elif record['sanad_stat'] == 'EDARI':
        document = 4
    elif record['sanad_stat'] == 'GHOLNAMEI':
        document = 5
    elif record['sanad_stat'] == 'TAVONI':
        document = 6
    elif record['sanad_stat'] == 'OGHAFI':
        document = 7
    elif record['sanad_stat'] == 'BONYADI':
        document = 8
    elif record['sanad_stat'] == 'MOSHA':
        document = 9
    elif record['sanad_stat'] == 'DARDASTEGHDAM':
        document = 10
    else:
        document = 1

    if record['deal_type'] == 'EJARE':
        transaction = 1
    elif record['deal_type'] == 'KHARID':
        transaction = 2
    else:
        transaction = record['deal_type']

    equipments = []
    for facilitie in record['facilities']:
        equipments.append(facilitie)
    for tasisat in record['tasisat']:
        equipments.append(tasisat)
    for other_facilities in str(record['other_facilities']).split(','):
        equipments.append(other_facilities)
    equipmentDict = {
        "SHOFAZH":0, "KOOLER_ABI":1, "KOOLER_GAZI":1, "GAZ":2, "CHILER":3, "PAKAGE":6, "GARMAYESH_AZ_KAF":10,
        "ASANSOR":13, "REMOTEDOOR":15, "LABI":30, "DOZDGIR":39, "CHAH":41, "DAKTSPILET":45, "MOBLEH":47, "AB":61,
        "BARGH":62, "IPHONE":64, "ANBARI":67, "HOME_SERAIDAR":68, "SERAIDAR":68, "SONA":69, "CHAKOZI":70, "PARKING":71,
        "BALKON":72, "ESTAKHR":73,
    }
    if action == 1:
        estate = models.Estate(
            user_id=None, data_id=record['elead_id'], estate_type_id=estType, installation=None,
            name=record['owner_name'], area=record['size_subs'], land_area=None, age=age, front_length=None,
            direction=directionL, rooms_count=record['rooms'], floors_count=record['floors'], units_count=None,
            floor=record['floor'], total_units_count=None, cover=record['flooring'], frontage=record['view_material'],
            wc=record['toilet'], kitchen=None, document=document, has_building=None, habitation=habitation,
            address=record['est_address'], postal_code=None, map=map, mobile=mobile, phone=phone, fronts_count=None,
            lines_count=None, has_modify=record['eslahi'], allocation_type=None,
            has_manufacturing_license=record['javaz_sakht'], has_wall=record['wall_cover'], has_landscaping=None,
            vegetation=None, car_way=None, urban_position=None, is_habitable=None, has_agricultural_water=None,
            has_endofwork=None, distance_from_asphalt=None, updated_by=None, active=None, created_at=None,
            updated_at=None
        )
        estate.save()
        for obj in equipments:
            if obj in equipmentDict:
                print(equipmentDict[obj])
                equipment = models.Equipment.objects.get(number=equipmentDict[obj])
                estate.equipments.add(equipment)
        advertisement = models.Advertisement(
            user_id=None, agent_id=None, transaction_type_id=transaction, reject_id=None, title=None, slug=None,
            settlement_sale_price=None, estate_id=estate.id,
            sale_price=record['price'], settlement_rent_price=None, mortgage_only=record['price_rahn'],
            mortgage_price=None,
            rent_price=record['price_rent'],
            sale_situation=None, has_loan=None,
            status=None, is_special=None, description=None, expired_at=None, updated_by=None, visit=None, active=None,
            created_at=None, updated_at=None,
        )
        advertisement.save()
        return estate, advertisement
    if action == 2:
        a = 2


def JSON(record):
    schema = {
        "estate":{
            "id":None,
            "user_id":None,
            "data_id":record.estate.data_id,
            # "estate_type_id":estType,
            # "installation":None,
            # "name":record['owner_name'],
            # "area":record['size_subs'],
            # "land_area":None,
            # "age":age,
            # "front_length":None,
            # "direction":directionL,
            # "rooms_count":record['rooms'],
            # "floors_count":record['floors'],
            # "units_count":None,
            # "floor":record['floor'],
            # "total_units_count":None,
            # "cover":record['flooring'],
            # "frontage":record['view_material'],
            # "wc":record['toilet'],
            # "kitchen":None,
            # "document":document,
            # "has_building":None,
            # "habitation":habitation,
            # "address":record['est_address'],
            # "postal_code":None,
            # "map":map,
            # "mobile":mobile,
            # "phone":phone,
            # "fronts_count":None,
            # "lines_count":None,
            # "has_modify":record['eslahi'],
            # "allocation_type":None,
            # "has_manufacturing_license":record['javaz_sakht'],
            # "has_wall":record['wall_cover'],
            "has_landscaping":None,
            "vegetation":None,
            "car_way":None,
            "urban_position":None,
            "is_habitable":None,
            "has_agricultural_water":None,
            "has_endofwork":None,
            "distance_from_asphalt":None,
            "updated_by":None,
            "active":None,
            "created_at":None,
            "updated_at":None,
        },
        "equipments":[],
        "advertisement":{
            "id":None,
            "user_id":None,
            "agent_id":None,
            "estate_id":None,
            "transaction_type_id":record.transaction_type_id,
            "reject_id":None,
            "title":None,
            "slug":None,
            "settlement_sale_price":None,
            "sale_price":None,
            "settlement_rent_price":None,
            "mortgage_only":None,
            "mortgage_price":None,
            "rent_price":None,
            "sale_situation":None,
            "has_loan":None,
            "status":None,
            "is_special":None,
            "description":None,
            "expired_at":None,
            "updated_by":None,
            "visit":None,
            "active":None,
            "created_at":None,
            "updated_at":None,
        }
    }
    return schema
