import sys

from distance import lonlat_distance
from geocoder import get_ll_span
from mapapi_PG import show_map
from to_try import get_nearest_bisness


def main():
    # Берём адрес из командной строки
    toponym_to_find = ' '.join(sys.argv[1:])
    if toponym_to_find:
        # ll - координаты введённого объекта
        ll, spn = get_ll_span(toponym_to_find)
        json_data = get_nearest_bisness(ll, 'Аптека')
        # print(json_data)
        # адреса и названия аптеки, времени её работы, а также расстояния до неё от исходной точки
        snippet = {
            'address': json_data['properties']['description'],
            'name': json_data['properties']['name'],
            'working time': json_data['properties']['CompanyMetaData']['Hours']['text'],
            'distance from the point': lonlat_distance([float(x) for x in ll.split(',')],
                                                       json_data['geometry']['coordinates'])
        }
        for key, value in snippet.items():
            print(key, value, sep=' ----- ')
        # print(snippet)
        point = json_data['geometry']['coordinates']
        ll1 = "{0},{1}".format(point[0], point[1])
        show_map(add_params='pt={0},pm2dgl~{1},pm2ntl'.format(ll1, ll))
    else:
        print('Nop')


if __name__ == '__main__':
    main()
