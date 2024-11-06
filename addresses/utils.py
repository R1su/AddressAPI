import requests
from django.conf import settings


def geocode_address(address):
    url = 'https://geocode-maps.yandex.ru/1.x/'
    params = {
        'apikey': settings.YANDEX_GEOCODER_API_KEY,
        'geocode': address,
        'format': 'json',
    }
    response = requests.get(url, params=params)

    if response.status_code == 200:
        geo_data = response.json()
        components = geo_data['response']['GeoObjectCollection']['featureMember'][0][
            'GeoObject'
        ]['metaDataProperty']['GeocoderMetaData']['Address']['Components']

        city = next(
            (comp['name'] for comp in components if comp['kind'] == 'locality'), ''
        )
        street = next(
            (comp['name'] for comp in components if comp['kind'] == 'street'), ''
        )
        building = next(
            (comp['name'] for comp in components if comp['kind'] == 'house'), ''
        )

        return {'city': city, 'street': street, 'building': building}

    return None
