import sys
import arcpy

PROVINCE_CODES = ['BC', 'AB', 'SK', 'MB', 'ON', 'QC', 'NB', 
                  'PE', 'NS', 'NL', 'YT', 'NT', 'NU']
DATA_WORKSPACE = r'..\..\..\..\data\Canada\Canada.gdb'


def print_usage_and_exit():
    print('Usage: cursor03.py prov')
    print(f'where prov is one of {", ".join(PROVINCE_CODES)}')
    sys.exit(1)


def main():
    if len(sys.argv) != 2:
        print_usage_and_exit()

    prov = sys.argv[1].upper()
    if prov not in PROVINCE_CODES:
        print(f'Invalid province. Must be one of {", ".join(PROVINCE_CODES)}')
        sys.exit(1)

    arcpy.env.workspace = DATA_WORKSPACE
    prov_field = arcpy.AddFieldDelimiters(DATA_WORKSPACE, 'Prov')
    where_clause = f"{prov_field} = '{prov}'"
    feature_class = 'MajorCities'

    print('Name, Prov')
    try:
        with arcpy.da.SearchCursor(feature_class, ['Name', 'Prov'], where_clause=where_clause) as cursor:
            count = 0
            for row in cursor:
                name, province = row
                print(f'{name}, {province}')
                count += 1
    except arcpy.ExecuteError:
        print('Error occurred while accessing data.')
        sys.exit(1)

    print(f'There are {count} cities in the above list')


if __name__ == '__main__':
    main()
