import googlemaps
from key import api_key

def get_geolocation(api_key):
    gmaps = googlemaps.Client(key=api_key)

    try:
        # Request user's location
        user_location = gmaps.geolocate()

        # Extract latitude and longitude
        latitude = user_location['location']['lat']
        longitude = user_location['location']['lng']

        # Reverse geocode to get address components
        reverse_geocode_result = gmaps.reverse_geocode((latitude, longitude))
        
        # Extract city, state, and country from the result
        for address_component in reverse_geocode_result[0]['address_components']:
            if 'locality' in address_component['types']:
                city = address_component['long_name']
            elif 'administrative_area_level_1' in address_component['types']:
                state = address_component['long_name']
            elif 'country' in address_component['types']:
                country = address_component['long_name']
        
        return city, state, country
    except googlemaps.exceptions.ApiError as e:
        print("Error occurred:", e)
        return None, None, None

# Call the function to get user's geolocation
city, state, country = get_geolocation(api_key)

if city is not None and state is not None and country is not None:
    print("City:", city)
    print("State:", state)
    print("Country:", country)
else:
    print("Failed to retrieve user's geolocation.")