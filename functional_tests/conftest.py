import pytest

from faker import Faker
from providers.custom import CustomProvider


faker = Faker()
faker.add_provider(CustomProvider)


@pytest.fixture(scope='session')
def get_location_search_api_url():
    """Returns the API URL for Location Search"""
    return "https://www.metaweather.com/api/location/search/"


@pytest.fixture(scope='session')
def get_location_api_url():
    """Returns the API URL for Location & Location Day"""
    return "https://www.metaweather.com/api/location"


@pytest.fixture(scope='session')
def location_search_query_param():
    """
        Returns the Valid City Name for Location Search
            based on the Test Data provided in provider file.
    """
    query = faker.valid_cities()
    return query


@pytest.fixture(scope='session')
def location_search_query_subset_param():
    """
        Returns the Valid subset of City Name for Location Search
            based on the Test Data provided in provider file.
    """
    query = faker.valid_cities_substring()
    return query


@pytest.fixture(scope='session')
def location_search_lattlong_valid():
    """
        Returns the Valid Latitude & Longitude values for Location Search
            based on the Test Data provided in provider file.
    """
    lattlong = faker.valid_lattlong()
    return lattlong


@pytest.fixture(scope='session')
def location_search_lattlong_invalid():
    """
        Returns the Invalid Latitude & Longitude values for Location Search
            based on the Test Data provided in provider file.
    """
    lattlong = faker.invalid_lattlong()
    return lattlong


@pytest.fixture(scope='session')
def get_random_latt_long():
    """
        Returns the random valid Latitude & Longitude values for
            Location Search generated using faker get location on land.
    """
    lat, longt = faker.location_details_gen('lattlong')
    lattlong = f"{lat},{longt}"
    return lattlong


@pytest.fixture(scope='session')
def get_random_city():
    """
        Returns the random valid City Name for Location Search 
            generated using faker get location on land.
    """
    return faker.location_details_gen('city')


@pytest.fixture(scope='session')
def get_valid_woeid():
    """
        Returns a valid Where On Earth ID(woeid) based on the 
            Test Date in the providers
    """
    return faker.valid_woeid()

@pytest.fixture(scope='session')
def get_valid_date():
    """
        Returns a valid Date for which the data in the test JSON 
            can be verified
    """
    return faker.valid_dates()