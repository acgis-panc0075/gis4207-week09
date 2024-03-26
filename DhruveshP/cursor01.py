import arcpy

def print_city_prov(city, prov):
    print(f'{city}, {prov}')

def count_cities(features):
    count = 0
    for city, prov in features:
        count += 1
        print_city_prov(city, prov)
    return count

def main():
    fc_path = r'..\..\..\..\data\Canada\Can_Mjr_Cities.shp'
    fields = ['Name', 'Prov']

    print('Name, Prov')
    with arcpy.da.SearchCursor(fc_path, fields) as cursor:
        cities = [(row[0], row[1]) for row in cursor]
    
    num_cities = count_cities(cities)
    print(f'There are {num_cities} cities in the above list')

if __name__ == "__main__":
    main()
