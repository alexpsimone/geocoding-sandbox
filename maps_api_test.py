import os
import requests

api_key = os.environ['GOOGLE_MAPS_API_KEY']

# Google Places API Example


"""OPTION 1: Find lat/lon of Zip, then use as center of Places search w/radius"""
# zip_code = 60016
# location_bias_center_payload = {
#     'address': zip_code,
#     'key': api_key
# }
# location_bias_center_url = 'https://maps.googleapis.com/maps/api/geocode/json'

# location_bias_center_res = requests.get(location_bias_center_url, params = location_bias_center_payload)
# location_bias_center_data = location_bias_center_res.json()
# print(location_bias_center_data)

# location_bias_center_data = {'results': [{'address_components': [{'long_name': '60016', 'short_name': '60016', 'types': ['postal_code']}, {'long_name': 'Des Plaines', 'short_name': 'Des Plaines', 'types': ['locality', 'political']}, {'long_name': 'Cook County', 'short_name': 'Cook County', 'types': ['administrative_area_level_2', 'political']}, {'long_name': 'Illinois', 'short_name': 'IL', 'types': ['administrative_area_level_1', 'political']}, {'long_name': 'United States', 'short_name': 'US', 'types': ['country', 'political']}], 'formatted_address': 'Des Plaines, IL 60016, USA', 'geometry': {'bounds': {'northeast': {'lat': 42.0806391, 'lng': -87.840318}, 'southwest': {'lat': 42.025905, 'lng': -87.942379}}, 'location': {'lat': 42.0488548, 'lng': -87.8844309}, 'location_type': 'APPROXIMATE', 'viewport': {'northeast': {'lat': 42.0806391, 'lng': -87.840318}, 'southwest': {'lat': 42.025905, 'lng': -87.942379}}}, 'place_id': 'ChIJWZImXoG3D4gREMpGWo-Ejds', 'types': ['postal_code']}], 'status': 'OK'}

# for item in location_bias_center_data['results']['address_components']:
#     print('**************************************************************************************')
#     print(item)
#     print('**************************************************************************************')


"""OPTION 2: Just do a Places Search with text string from facility data"""
# payload = {
    
#     'input': 'Weill Foot & Ankle Institute Des Plains Illinois 60016 United States',
#     'inputtype': 'textquery',
#     'fields': 'formatted_address,name,opening_hours,geometry',
#     'key': api_key,
# }

# url = f'https://maps.googleapis.com/maps/api/place/findplacefromtext/json'


"""OPTION 3: Do a Geocoding Search with text string from facility data"""
# Google Geocoding API Example
# payload = {
#     'address': 'Weill Foot & Ankle Institute Des Plaines Illinois 60016 United States',
#     'key': api_key
# }
# url = 'https://maps.googleapis.com/maps/api/geocode/json'



# res = requests.get(url, params = payload)
# data = res.json()
# print(data)




# data = {'results': [{'address_components': [{'long_name': '1455', 'short_name': '1455', 'types': ['street_number']}, {'long_name': 'East Golf Road', 'short_name': 'E Golf Rd', 'types': ['route']}, {'long_name': 'Des Plaines', 'short_name': 'Des Plaines', 'types': ['locality', 'political']}, {'long_name': 'Maine Township', 'short_name': 'Maine Township', 'types': ['administrative_area_level_3', 'political']}, {'long_name': 'Cook County', 'short_name': 'Cook County', 'types': ['administrative_area_level_2', 'political']}, {'long_name': 'Illinois', 'short_name': 'IL', 'types': ['administrative_area_level_1', 'political']}, {'long_name': 'United States', 'short_name': 'US', 'types': ['country', 'political']}, {'long_name': '60016', 'short_name': '60016', 'types': ['postal_code']}, {'long_name': '1250', 'short_name': '1250', 'types': ['postal_code_suffix']}], 'formatted_address': '1455 E Golf Rd, Des Plaines, IL 60016, USA', 'geometry': {'location': {'lat': 42.0541518, 'lng': -87.8886498}, 'location_type': 'ROOFTOP', 'viewport': {'northeast': {'lat': 42.0555007802915, 'lng': -87.8873008197085}, 'southwest': {'lat': 42.0528028197085, 'lng': -87.8899987802915}}}, 'partial_match': True, 'place_id': 'ChIJBSoioYa3D4gRRfU73Nfc5n0', 'plus_code': {'compound_code': '3436+MG Des Plaines, IL, USA', 'global_code': '86JJ3436+MG'}, 'types': ['doctor', 'establishment', 'health', 'point_of_interest']}], 'status': 'OK'}

# for item in data['results']:
#     print('**************************************************************************************')
#     for component in item['address_components']:
#         print(component)
#     print('**************************************************************************************')


# data = {'candidates': [{'formatted_address': '1455 E Golf Rd, Des Plaines, IL 60016, United States', 'geometry': {'location': {'lat': 42.0541518, 'lng': -87.8886498}, 'viewport': {'northeast': {'lat': 42.05560227989272, 'lng': -87.88730567010728}, 'southwest': {'lat': 42.05290262010728, 'lng': -87.89000532989273}}}, 'name': 'Lowell S. Weil Sr, DPM'}, {'formatted_address': '1660 Feehanville Dr Ste 100, Mt Prospect, IL 60056, United States', 'geometry': {'location': {'lat': 42.0786026, 'lng': -87.9094988}, 'viewport': {'northeast': {'lat': 42.07995432989271, 'lng': -87.90831137010727}, 'southwest': {'lat': 42.07725467010727, 'lng': -87.91101102989272}}}, 'name': 'Weil Foot & Ankle Institute', 'opening_hours': {'open_now': True}}], 'status': 'OK'}

# for item in data['candidates']:
#     print('**************************************************************************************')
#     print(item['name'])
#     print(item['formatted_address'])
#     print('lat:', item['geometry']['location']['lat'])
#     print('lon:', item['geometry']['location']['lng'])
#     print('**************************************************************************************')


"""OPTION 4: Do a Nearby Places Search with text string from facility data"""

nearby_url = 'https://maps.googleapis.com/maps/api/place/nearbysearch/json'
nearby_payload = {
    'key': api_key,
    
}