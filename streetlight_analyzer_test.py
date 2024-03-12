import streetlight_analyzer

streetlight_analyzer.data_file = "path_to_your_data_file.csv"
streetlight_analyzer.road_name_field = "ROAD_NAME_"

def test_load_streetlights_data():
    streetlight_analyzer.load_streetlights_data()
    
    assert streetlight_analyzer.streetlights_data is not None
    
    assert len(streetlight_analyzer.streetlights_data) > 0

test_load_streetlights_data()

