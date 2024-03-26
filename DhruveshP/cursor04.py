import sys

prov_codes = ['BC', 'AB', 'SK', 'MB', 'ON', 'QC', 'NB', 
              'PE', 'NS', 'NL', 'YT', 'NT', 'NU']
                    
    
def main():
    if len(sys.argv) != 2:
        print('Usage: cursor04.py prov')
        print(f'where prov is one of {", ".join(prov_codes)}')
        exit()

    prov = sys.argv[1].upper()
    if prov not in prov_codes:
        print (f'Invalid prov.  Must be one of {", ".join(prov_codes)}')
        exit()

    import arcpy

    ws = r'..\..\..\..\data\Canada\Canada.gdb'
    arcpy.env.workspace = ws
    prov_field = arcpy.AddFieldDelimiters(ws, 'Prov')
    wc =  f"{prov_field}='{prov}'"
    fc = 'MajorCities'
    print ('Name,Prov,Longitude,Latitude')
    with arcpy.da.SearchCursor(fc, 
                               ['Name', 'Prov', 'SHAPE@XY'], 
                               where_clause=wc) as cursor:
        count = 0
        for row in cursor:
            count += 1
            name = row[0]
            prov = row[1]
            longitude = row[2][0]
            latitude = row[2][1]
            print (f'{name},{prov},{longitude},{latitude}')
        print (f'There are {count} cities in the above list')


if __name__ == '__main__':
    main()