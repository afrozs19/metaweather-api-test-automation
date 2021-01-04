from faker import Faker
import random
import time
from datetime import timedelta, date
from faker.providers import BaseProvider

VALID_CITIES = [
    "Berlin",
    "London",
    "Singapore",
    "Pune"
]

VALID_CITIES_SUBSTRING = [
    "San",
    "Ber",
    "Tor"
]

VALID_WOEID = [
    44418,
    638242,
    2295412,
    1062617
]

VALID_LATTLONG = [
    "55.9533, -3.1883",
    "19.0760, 72.8777"
]

INVALID_LATTLONG = [
    "55.95.33, -3.18.83",
    "abc, xyz",
    "19.07.60, 72.8777"
]

VALID_DATES = [
    "2020/12/30",
    "2019/08/19"
]

faker = Faker()

class CustomProvider(BaseProvider):


    def valid_cities(self):
        """Return a random valid city from the list defined above"""
        return random.choice(VALID_CITIES)

    def valid_cities_substring(self):
        """Return a random substring for a city from the list defined above"""
        return random.choice(VALID_CITIES_SUBSTRING)

    def valid_lattlong(self):
        """Return a random set of valid Lattitude Longitude values"""
        return random.choice(VALID_LATTLONG)

    def invalid_lattlong(self):
        """Return a random set of invalid Lattitude Longitude values"""
        return random.choice(INVALID_LATTLONG)

    def location_details_gen(self, args):
        """Returns a random City, Latitude, Longitude, Code or Timezone"""
        lat, longt, city, code, timezone = faker.location_on_land()

        if args == 'lattlong':
            return lat, longt
        
        elif args == 'city':
            return city
        
        elif args == 'timezone':
            return timezone
        
        elif args == 'code':
            return code
    
    def valid_woeid(self):
        """Return a random woeid from the list defined above"""
        return random.choice(VALID_WOEID)
    
    def valid_dates(self):
        """Return a random date from the list defined above"""
        return random.choice(VALID_DATES)