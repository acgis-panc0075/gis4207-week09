import arcpy
import zipfile

def main():
    ws = r'..\..\..\..\data\Canada\Canada.gdb'
    fc = 'MajorCities'
    
    arcpy.env.workspace = ws

    field_names = ['Name', 'UTM_MAP', 'SHAPE@XY']
    with open(r'..\output\Cities.kml', 'w') as outfile:
        outfile.write(get_kml_header())
        with arcpy.da.SearchCursor(fc, field_names) as cursor:
            for row in cursor:
                name = row[0]
                utm_map = row[1]
                longitude = row[2][0]
                latitude = row[2][1]
                pm = get_placemark(name, longitude, latitude, utm_map)
                outfile.write(pm)                      
        outfile.write(get_kml_footer())

    out_kmz_name = r'..\output\cities.kmz'
    zf = zipfile.ZipFile(out_kmz_name, 'w', zipfile.ZIP_DEFLATED)
    zf.compression
    zf.write(r"..\output\cities.kml")
    zf.close()


def get_kml_header():
    kml = """<?xml version="1.0" encoding="UTF-8"?> \
           <kml xmlns="http://www.opengis.net/kml/2.2">\
           <Document>
          """
    return kml


def get_placemark(name,longitude,latitude,utm_map):
    url = f'http://www.canmaps.com/topo/nts50/map/{utm_map.lower()}.htm'
    return f"""<Placemark><name>{name}</name>
    <description>
      {url}
    </description>
    <Point>
      <coordinates>{longitude},{latitude},0</coordinates>
    </Point>
    </Placemark>"""


def get_kml_footer():
    return '  </Document>\n</kml>'


if __name__ == '__main__':
    main()