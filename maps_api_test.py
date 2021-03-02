import os
import requests
# reference list of lat/lng for zip codes found at https://gist.github.com/erichurst/7882666

api_key = os.environ['GOOGLE_MAPS_API_KEY']


"""
##################################################################################################
##################################################################################################
# OPTION 1: Find lat/lon of Zip, then use as center of Places search w/radius.
#
# This doesn't seem to provide any more relevant results than a regular places search.
##################################################################################################
##################################################################################################
"""
zip_code = 60016
location_bias_center_payload = {
    'address': zip_code,
    'key': api_key
}
location_bias_center_url = 'https://maps.googleapis.com/maps/api/geocode/json'

# location_bias_center_res = requests.get(location_bias_center_url, params = location_bias_center_payload)
# location_bias_center_data = location_bias_center_res.json()
# print(location_bias_center_data)

# location_bias_center_data = {'results': [{'address_components': [{'long_name': '60016', 'short_name': '60016', 'types': ['postal_code']}, {'long_name': 'Des Plaines', 'short_name': 'Des Plaines', 'types': ['locality', 'political']}, {'long_name': 'Cook County', 'short_name': 'Cook County', 'types': ['administrative_area_level_2', 'political']}, {'long_name': 'Illinois', 'short_name': 'IL', 'types': ['administrative_area_level_1', 'political']}, {'long_name': 'United States', 'short_name': 'US', 'types': ['country', 'political']}], 'formatted_address': 'Des Plaines, IL 60016, USA', 'geometry': {'bounds': {'northeast': {'lat': 42.0806391, 'lng': -87.840318}, 'southwest': {'lat': 42.025905, 'lng': -87.942379}}, 'location': {'lat': 42.0488548, 'lng': -87.8844309}, 'location_type': 'APPROXIMATE', 'viewport': {'northeast': {'lat': 42.0806391, 'lng': -87.840318}, 'southwest': {'lat': 42.025905, 'lng': -87.942379}}}, 'place_id': 'ChIJWZImXoG3D4gREMpGWo-Ejds', 'types': ['postal_code']}], 'status': 'OK'}

# for item in location_bias_center_data['results']:
#     print('**************************************************************************************')
#     print(item)
#     print('**************************************************************************************')


"""
##################################################################################################
##################################################################################################
# OPTION 2: Just do a Places Search with text string from facility data.
#
# This might return too few results.
# Omitting the country name seemed to help return more results (WHY?)
# Locationbias didn't seem to help.
##################################################################################################
##################################################################################################
"""
payload = {

    'input': 'Weill Foot & Ankle Institute Des Plains Illinois 60016 United States',
    'inputtype': 'textquery',
    'fields': 'formatted_address,name,opening_hours,geometry',
    'key': api_key
    # 'locationbias': '161000@42.049573, -87.895003'
}

url = 'https://maps.googleapis.com/maps/api/place/findplacefromtext/json'

# res = requests.get(url, params = payload)
# data = res.json()
# print(data)

# # data = {'candidates': [{'formatted_address': '1455 E Golf Rd, Des Plaines, IL 60016, United States', 'geometry': {'location': {'lat': 42.0541518, 'lng': -87.8886498}, 'viewport': {'northeast': {'lat': 42.05560227989272, 'lng': -87.88730567010728}, 'southwest': {'lat': 42.05290262010728, 'lng': -87.89000532989273}}}, 'name': 'Lowell S. Weil Sr, DPM'}, {'formatted_address': '1660 Feehanville Dr Ste 100, Mt Prospect, IL 60056, United States', 'geometry': {'location': {'lat': 42.0786026, 'lng': -87.9094988}, 'viewport': {'northeast': {'lat': 42.07995432989271, 'lng': -87.90831137010727}, 'southwest': {'lat': 42.07725467010727, 'lng': -87.91101102989272}}}, 'name': 'Weil Foot & Ankle Institute', 'opening_hours': {'open_now': True}}], 'status': 'OK'}

# for item in data['candidates']:
#     print('**************************************************************************************')
#     print(item['name'])
#     print(item['formatted_address'])
#     print('lat:', item['geometry']['location']['lat'])
#     print('lon:', item['geometry']['location']['lng'])
#     print('**************************************************************************************')


"""
##################################################################################################
##################################################################################################
# OPTION 3: Do a Geocoding Search with text string from facility data
#
# I don't think this works since many of the searches will include business names.
# Google Maps Geocoding API explicitly says to avoid using this info in a search.
##################################################################################################
##################################################################################################
"""
payload = {
    'address': 'Weill Foot & Ankle Institute Des Plaines Illinois 60016 United States',
    'key': api_key
}
url = 'https://maps.googleapis.com/maps/api/geocode/json'

# res = requests.get(url, params = payload)
# data = res.json()
# print(data)


# data = {'results': [{'address_components': [{'long_name': '1455', 'short_name': '1455', 'types': ['street_number']}, {'long_name': 'East Golf Road', 'short_name': 'E Golf Rd', 'types': ['route']}, {'long_name': 'Des Plaines', 'short_name': 'Des Plaines', 'types': ['locality', 'political']}, {'long_name': 'Maine Township', 'short_name': 'Maine Township', 'types': ['administrative_area_level_3', 'political']}, {'long_name': 'Cook County', 'short_name': 'Cook County', 'types': ['administrative_area_level_2', 'political']}, {'long_name': 'Illinois', 'short_name': 'IL', 'types': ['administrative_area_level_1', 'political']}, {'long_name': 'United States', 'short_name': 'US', 'types': ['country', 'political']}, {'long_name': '60016', 'short_name': '60016', 'types': ['postal_code']}, {'long_name': '1250', 'short_name': '1250', 'types': ['postal_code_suffix']}], 'formatted_address': '1455 E Golf Rd, Des Plaines, IL 60016, USA', 'geometry': {'location': {'lat': 42.0541518, 'lng': -87.8886498}, 'location_type': 'ROOFTOP', 'viewport': {'northeast': {'lat': 42.0555007802915, 'lng': -87.8873008197085}, 'southwest': {'lat': 42.0528028197085, 'lng': -87.8899987802915}}}, 'partial_match': True, 'place_id': 'ChIJBSoioYa3D4gRRfU73Nfc5n0', 'plus_code': {'compound_code': '3436+MG Des Plaines, IL, USA', 'global_code': '86JJ3436+MG'}, 'types': ['doctor', 'establishment', 'health', 'point_of_interest']}], 'status': 'OK'}

# for item in data['results']:
#     print('**************************************************************************************')
#     for component in item['address_components']:
#         print(component)
#     print('**************************************************************************************')


"""
##################################################################################################
##################################################################################################
# OPTION 4: Do a Nearby Places Search with text string from facility data
#
# TOO EXPENSIVE - approx $9k for entire dataset.
# This does return the most useful results, though!
##################################################################################################
##################################################################################################
"""
nearby_url = 'https://maps.googleapis.com/maps/api/place/nearbysearch/json'
nearby_payload = {
    'key': api_key,
    'location': '42.049573,-87.895003',
    'rankby': 'distance',
    'keyword': 'Weill Foot & Ankle Institute Des Plains Illinois 60016 United States'
}

# res = requests.get(nearby_url, params = nearby_payload)
# data = res.json()
# print(data)

nearby_data = {'html_attributions': [], 'results': [{'business_status': 'OPERATIONAL', 'geometry': {'location': {'lat': 42.0538843, 'lng': -87.8890225}, 'viewport': {'northeast': {'lat': 42.05546247989272, 'lng': -87.88768567010729}, 'southwest': {'lat': 42.05276282010728, 'lng': -87.89038532989272}}}, 'icon': 'https://maps.gstatic.com/mapfiles/place_api/icons/v1/png_71/generic_business-71.png', 'name': 'Foot & Ankle Surgical Center', 'opening_hours': {'open_now': True}, 'place_id': 'ChIJBSoioYa3D4gRP6rwumgaOjU', 'plus_code': {'compound_code': '3436+H9 Des Plaines, Illinois', 'global_code': '86JJ3436+H9'}, 'rating': 5, 'reference': 'ChIJBSoioYa3D4gRP6rwumgaOjU', 'scope': 'GOOGLE', 'types': ['health', 'point_of_interest', 'establishment'], 'user_ratings_total': 1, 'vicinity': '1455 E Golf Rd, Des Plaines'}, {'business_status': 'OPERATIONAL', 'geometry': {'location': {'lat': 42.0541518, 'lng': -87.8886498}, 'viewport': {'northeast': {'lat': 42.05560227989272, 'lng': -87.88730567010728}, 'southwest': {'lat': 42.05290262010728, 'lng': -87.89000532989273}}}, 'icon': 'https://maps.gstatic.com/mapfiles/place_api/icons/v1/png_71/generic_business-71.png', 'name': 'Lowell S. Weil Sr, DPM', 'place_id': 'ChIJBSoioYa3D4gRRfU73Nfc5n0', 'plus_code': {'compound_code': '3436+MG Des Plaines, Illinois', 'global_code': '86JJ3436+MG'}, 'rating': 4.8, 'reference': 'ChIJBSoioYa3D4gRRfU73Nfc5n0', 'scope': 'GOOGLE', 'types': ['doctor', 'health', 'point_of_interest', 'establishment'], 'user_ratings_total': 4, 'vicinity': '1455 E Golf Rd, Des Plaines'}, {'business_status': 'OPERATIONAL', 'geometry': {'location': {'lat': 42.054904, 'lng': -87.889805}, 'viewport': {'northeast': {'lat': 42.05615267989272, 'lng': -87.88844792010727}, 'southwest': {'lat': 42.05345302010728, 'lng': -87.8911475798927}}}, 'icon': 'https://maps.gstatic.com/mapfiles/place_api/icons/v1/png_71/generic_business-71.png', 'name': 'Illinois Foot & Ankle Clinic', 'opening_hours': {'open_now': True}, 'photos': [{'height': 626, 'html_attributions': ['<a href="https://maps.google.com/maps/contrib/113399095546386807636">A Google User</a>'], 'photo_reference': 'ATtYBwLDsNTdt9JFj6Qy-Cik7Z8RVnLS1MVSpJOtTaAiDrOqnCF5NHkB4Z-gUSh29hsUUMkGFkElfvChXdKr3tixtKDHTS7Qz1lPXkjr9suSYVZV9oxnUX4HbqX5BWD2T07KvULudWjnbIPXcBJ4oXYoxw17YcLUE9WGZG2jB2ZcsOaL4EM1', 'width': 1080}], 'place_id': 'ChIJm5zb63aoD4gRPvmosr-1rsQ', 'plus_code': {'compound_code': '3436+X3 Des Plaines, Illinois', 'global_code': '86JJ3436+X3'}, 'rating': 4.2, 'reference': 'ChIJm5zb63aoD4gRPvmosr-1rsQ', 'scope': 'GOOGLE', 'types': ['doctor', 'health', 'point_of_interest', 'establishment'], 'user_ratings_total': 5, 'vicinity': '1400 E Golf Rd #201, Des Plaines'}, {'business_status': 'OPERATIONAL', 'geometry': {'location': {'lat': 42.0310749, 'lng': -87.89512669999999}, 'viewport': {'northeast': {'lat': 42.03251347989273, 'lng': -87.89378582010728}, 'southwest': {'lat': 42.02981382010729, 'lng': -87.89648547989272}}}, 'icon': 'https://maps.gstatic.com/mapfiles/place_api/icons/v1/png_71/generic_business-71.png', 'name': 'Midwest Foot and Ankle Center, PC', 'opening_hours': {'open_now': False}, 'photos': [{'height': 4032, 'html_attributions': ['<a href="https://maps.google.com/maps/contrib/105620892806774038340">A Google User</a>'], 'photo_reference': 'ATtYBwJIJUg_5A-CcaqmjxEtqYde0lNfwlXMC3a36ezw7jbe85M8_0S_AQ6qcGlZH8JUPqi0DVWmvZ70e9GO_E_CY_cWvjNr0J8cC7rLTBaJva-tCO2SCn-65PxpmuzyaHlG6fpbdCGHW2RfwefG-NTN18Nzf1qRGTsc2Li_uYv8CYD_k4eK', 'width': 3024}], 'place_id': 'ChIJt0X6ngm3D4gRbbTDXz8W_tc', 'plus_code': {'compound_code': '24J3+CW Des Plaines, Illinois', 'global_code': '86JJ24J3+CW'}, 'rating': 3, 'reference': 'ChIJt0X6ngm3D4gRbbTDXz8W_tc', 'scope': 'GOOGLE', 'types': ['doctor', 'health', 'point_of_interest', 'establishment'], 'user_ratings_total': 2, 'vicinity': '1167 E Algonquin Rd #1, Des Plaines'}, {'business_status': 'OPERATIONAL', 'geometry': {'location': {'lat': 42.0395754, 'lng': -87.8719941}, 'viewport': {'northeast': {'lat': 42.04098007989272, 'lng': -87.87057537010728}, 'southwest': {'lat': 42.03828042010727, 'lng': -87.87327502989272}}}, 'icon': 'https://maps.gstatic.com/mapfiles/place_api/icons/v1/png_71/generic_business-71.png', 'name': 'Global Foot and Ankle Clinic', 'opening_hours': {'open_now': False}, 'photos': [{'height': 470, 'html_attributions': ['<a href="https://maps.google.com/maps/contrib/113636300045938609662">Patty Anaya</a>'], 'photo_reference': 'ATtYBwKb8IzPGz_Ofs5VkyOSKjzWPjciebDpOXmdJNfFioj0Ruik-X60u3LNCbmXT98-lUFglccOSj5qZ9VL-Bc6K5YSrE-g0cj4Cc4_ZoykF1AMzIoP6ovhGPp5DtVR4BijEDMa4QJiL_kKmzdDqHOD1BF0Aj9DnsLqgV2v6r3Zhvw44WlD', 'width': 640}], 'place_id': 'ChIJGeSBGpq3D4gRd1ei7tnQWRw', 'plus_code': {'compound_code': '24QH+R6 Des Plaines, Illinois', 'global_code': '86JJ24QH+R6'}, 'rating': 5, 'reference': 'ChIJGeSBGpq3D4gRd1ei7tnQWRw', 'scope': 'GOOGLE', 'types': ['doctor', 'health', 'point_of_interest', 'establishment'], 'user_ratings_total': 5, 'vicinity': '2118 Miner St, Des Plaines'}, {'business_status': 'OPERATIONAL', 'geometry': {'location': {'lat': 42.0786026, 'lng': -87.9094988}, 'viewport': {'northeast': {'lat': 42.07995432989271, 'lng': -87.90831137010727}, 'southwest': {'lat': 42.07725467010727, 'lng': -87.91101102989272}}}, 'icon': 'https://maps.gstatic.com/mapfiles/place_api/icons/v1/png_71/generic_business-71.png', 'name': 'Weil Foot & Ankle Institute', 'opening_hours': {'open_now': True}, 'photos': [{'height': 1464, 'html_attributions': ['<a href="https://maps.google.com/maps/contrib/116746123581451164318">A Google User</a>'], 'photo_reference': 'ATtYBwJT6xLwq3jjFFEpKmdSJHkBZ4mYMHFEP53gKjjlJqxIhqNB57OlKzQDiFi1eTaQOfmr9O6gycxRH3GB-s8VIXW7Xy1LSTalXSQLJWmSr80MqweDoTuQvGFZRMCrqSpwejQa01unn_j3A1N2B5yvAi87oHIV3VxolkBxbGMIfIphuLbP', 'width': 2742}], 'place_id': 'ChIJJUPu9Fy5D4gRuMwkU0MIznc', 'plus_code': {'compound_code': '33HR+C6 Mt Prospect, Illinois', 'global_code': '86JJ33HR+C6'}, 'rating': 4.9, 'reference': 'ChIJJUPu9Fy5D4gRuMwkU0MIznc', 'scope': 'GOOGLE', 'types': ['doctor', 'health', 'point_of_interest', 'establishment'], 'user_ratings_total': 289, 'vicinity': '1660 Feehanville Dr Ste 100, Mt Prospect'}, {'business_status': 'OPERATIONAL', 'geometry': {'location': {'lat': 42.0786026, 'lng': -87.9094988}, 'viewport': {'northeast': {'lat': 42.07995432989271, 'lng': -87.90831137010727}, 'southwest': {'lat': 42.07725467010727, 'lng': -87.91101102989272}}}, 'icon': 'https://maps.gstatic.com/mapfiles/place_api/icons/v1/png_71/generic_business-71.png', 'name': 'Dr. Gregory Amarantos DPM', 'opening_hours': {'open_now': True}, 'photos': [{'height': 1440, 'html_attributions': ['<a href="https://maps.google.com/maps/contrib/117503557741877439082">Sergey Dunaev</a>'], 'photo_reference': 'ATtYBwKFoQnzKY_ydKOwv7McGv2a8AgDXsuD8j8uAmMBVyabuAgEZjz-bbQ99IweUEb5TiJQ303SLv2VfMqutV4dgpBDPrDrWI_LuPT4gESrqJal--z8F5iIcVSUnuUarYC4qrm46eem1NUPewsntWRBhgGWpYPL7-HAw39saN4kTu-rV6RZ', 'width': 2560}], 'place_id': 'ChIJBSoioYa3D4gRarFZxwGpIfw', 'plus_code': {'compound_code': '33HR+C6 Mt Prospect, Illinois', 'global_code': '86JJ33HR+C6'}, 'rating': 3.4, 'reference': 'ChIJBSoioYa3D4gRarFZxwGpIfw', 'scope': 'GOOGLE', 'types': ['doctor', 'health', 'point_of_interest', 'establishment'], 'user_ratings_total': 5, 'vicinity': '1660 Feehanville Dr Ste 100, Mt Prospect'}, {'business_status': 'OPERATIONAL', 'geometry': {'location': {'lat': 42.0780904, 'lng': -87.79873160000001}, 'viewport': {'northeast': {'lat': 42.07943887989273, 'lng': -87.79727492010727}, 'southwest': {'lat': 42.07673922010728, 'lng': -87.79997457989272}}}, 'icon': 'https://maps.gstatic.com/mapfiles/place_api/icons/v1/png_71/generic_business-71.png', 'name': 'Weil Foot & Ankle Institute', 'opening_hours': {'open_now': True}, 'place_id': 'ChIJj5Z5azzGD4gR2AvYIayCMXU', 'plus_code': {'compound_code': '36H2+6G Glenview, Illinois', 'global_code': '86JJ36H2+6G'}, 'rating': 4.4, 'reference': 'ChIJj5Z5azzGD4gR2AvYIayCMXU', 'scope': 'GOOGLE', 'types': ['doctor', 'health', 'point_of_interest', 'establishment'], 'user_ratings_total': 14, 'vicinity': '1300 Waukegan Rd, Glenview'}, {'business_status': 'OPERATIONAL', 'geometry': {'location': {'lat': 42.13652270000001, 'lng': -87.9846979}, 'viewport': {'northeast': {'lat': 42.13782122989272, 'lng': -87.98334732010728}, 'southwest': {'lat': 42.13512157010728, 'lng': -87.98604697989273}}}, 'icon': 'https://maps.gstatic.com/mapfiles/place_api/icons/v1/png_71/generic_business-71.png', 'name': 'Weil Foot & Ankle Institute', 'opening_hours': {'open_now': True}, 'photos': [{'height': 3024, 'html_attributions': ['<a href="https://maps.google.com/maps/contrib/114277703639895228215">A Google User</a>'], 'photo_reference': 'ATtYBwJpYGfWiXXAQPGn8Mkm63olYg2cKOqdjj9Ir2xE72vU_5WPxi6IDtIMOIvKVFQ9gJSSqHE_AHG6J7il9-Fi6SAWL-X-70zc3d2lXsfOtJjjZck8w-jGobb3BeSQGwWHnjCfjJ1K-Zo4ihTNLoNAMBiYjXxJT9pa97UE8ECqYpxmaTug', 'width': 4032}], 'place_id': 'ChIJ8UUEWoW7D4gRRJaiB5MeCVk', 'plus_code': {'compound_code': '42P8+J4 Arlington Heights, Illinois', 'global_code': '86JJ42P8+J4'}, 'rating': 5, 'reference': 'ChIJ8UUEWoW7D4gRRJaiB5MeCVk', 'scope': 'GOOGLE', 'types': ['doctor', 'health', 'point_of_interest', 'establishment'], 'user_ratings_total': 7, 'vicinity': '3385 N Arlington Heights Rd Suite GH, Arlington Heights'}], 'status': 'OK'}

for item in data['results']:

    print('**************************************************************************************')
    print(item['name'])
    print(item['vicinity'])
    print('**************************************************************************************')