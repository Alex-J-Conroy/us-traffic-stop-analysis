# Importing Libraries needed for the reverse geocoding
!pip install  geopy
import geopy
import pandas as pd
import time
from tqdm import tqdm
tqdm.pandas()
from geopy.geocoders import Nominatim
geolocator = Nominatim(user_agent="your_app_name")
from geopy.extra.rate_limiter import RateLimiter
reverse = RateLimiter(geolocator.reverse, min_delay_seconds=1)


# function that takes the latitude and longitude from original data and pulls the full address from the API service.
df_h['Location'] = df_h.progress_apply(lambda row: reverse((row['lat'], row['lng'])),axis=1)
def parse_zipcode(location):
    if location and location.raw.get('address') and location.raw['address'].get('postcode'):
        return location.raw['address']['postcode']
    else:
        return None
    df_h['Zipcode'] = df_h['Location'].apply(parse_zipcode)
# writing the complete dataset to a csv.     
df_h.to_csv (r'Hart-2014-zip.csv', index = False, header=True)