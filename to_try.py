import requests

from mapapi_PG import show_map


def get_nearest_bisness(point, kind):
    search_api_server = 'https://search-maps.yandex.ru/v1/'
    search_params = {
        "apikey": "dda3ddba-c9ea-4ead-9010-f43fbc15c6e3",
        "text": kind,
        "lang": "ru_RU",
        "ll": point,
        "type": "biz"
    }

    response = requests.get(search_api_server, params=search_params)

    if not response:
        # ...
        pass

    # Преобразуем ответ в json-объект
    json_response = response.json()

    # Получаем первую найденную организацию.
    organization = json_response["features"][0]

    # Выдаём json

    return organization

    # Название организации.
    org_name = organization["properties"]["CompanyMetaData"]["name"]
    # Адрес организации.
    org_address = organization["properties"]["CompanyMetaData"]["address"]

    # Получаем координаты ответа.
    point = organization["geometry"]["coordinates"]
    org_point = "{0},{1}".format(point[0], point[1])
    delta = "0.005"

    # Собираем параметры для запроса к StaticMapsAPI:
    # добавим точку, чтобы указать найденную аптеку
    map_params = "pt={0},pm2dgl".format(org_point)
    ll_spn = f"ll={org_point}&spn{','.join([delta, delta])}"

    # ... и выполняем запрос
    show_map(ll_spn, add_params=map_params)
