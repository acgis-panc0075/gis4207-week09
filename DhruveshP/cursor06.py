import arcpy
import zipfile

def main():
    workspace = r'..\..\..\..\data\Canada\Canada.gdb'
    feature_class = 'MajorCities'
    
    arcpy.env.workspace = workspace

    field_names = ['Name', 'UTM_MAP', 'SHAPE@XY']
    
    with open(r'..\output\Cities.kml', 'w') as kml_file:
        kml_file.write(get_kml_header())  
        with arcpy.da.SearchCursor(feature_class, field_names) as cursor:
            for row in cursor:
                name, utm_map, (longitude, latitude) = row
                placemark = get_placemark(name, longitude, latitude, utm_map)
                kml_file.write(placemark)  
        kml_file.write(get_kml_footer()) 

    create_kmz_file()


def get_kml_header():
    return """<?xml version="1.0" encoding="UTF-8"?>
           <kml xmlns="http://www.opengis.net/kml/2.2">
           <Document>
          """


def get_placemark(name, longitude, latitude, utm_map):
    url = f'http://www.canmaps.com/topo/nts50/map/{utm_map.lower()}.htm'
    return f"""<Placemark>
    <name>{name}</name>
    <description>
      {url}
    </description>
    <Point>
      <coordinates>{longitude},{latitude},0</coordinates>
    </Point>
    </Placemark>"""


def get_kml_footer():
    return '  </Document>\n</kml>'


def create_kmz_file():
    out_kml = r'..\output\cities.kml'
    out_kmz = r'..\output\cities.kmz'
    
    with zipfile.ZipFile(out_kmz, 'w', zipfile.ZIP_DEFLATED) as kmz_file:
        kmz_file.write(out_kml, 'cities.kml')  


if __name__ == '__main__':
    main()
