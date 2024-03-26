import sys
import arcpy

PROV_CODES = ['BC', 'AB', 'SK', 'MB', 'ON', 'QC', 'NB', 
              'PE', 'NS', 'NL', 'YT', 'NT', 'NU']

def main():
    if len(sys.argv) != 2:
        print('Usage: cursor02.py prov')
        print(f'where prov is one of {", ".join(PROV_CODES)}')
        sys.exit(1)

    prov = sys.argv[1].upper()
    if prov not in PROV_CODES:
        print(f'Invalid province code. Must be one of {", ".join(PROV_CODES)}')
        sys.exit(1)

    workspace = r'..\..\..\..\data\Canada'
    arcpy.env.workspace = workspace
    prov_field = arcpy.AddFieldDelimiters(workspace, 'Prov')
    where_clause = f"{prov_field}='{prov}'"
    feature_class = 'Can_Mjr_Cities.shp'

    print('Name, Prov')
    count = 0
    with arcpy.da.SearchCursor(feature_class, ['Name', 'Prov'], where_clause=where_clause) as cursor:
        for row in cursor:
            count += 1
            name, prov = row[0], row[1]
            print(f'{name}, {prov}')
    
    print(f'There are {count} cities in the above list')

if __name__ == '__main__':
    main()
