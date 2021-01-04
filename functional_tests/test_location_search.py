import logging
import pytest
import requests
import allure
import utilities.custom_logger as cl

import resources.operations as ops
from utilities.read_json import readJson


@pytest.mark.LocationSearch
class TestLocationSearch:

    """
        URL:
            '/api/location/search/?query=(query)', '/api/location/search/?lattlong=(latt),(long)'
        
        Arguments:
            Either query or lattlong need to be present.\n
                'query' - 
                    Text to search for.
                'lattlong' - 
                    Coordinates to search for locations near. Comma separated lattitude and longitude e.g. "36.96,-122.02".
        
        Examples:
            Below are the list of examples.\n
                '/api/location/search/?query=san', 
                '/api/location/search/?query=london', 
                '/api/location/search/?lattlong=36.96,-122.02', 
                '/api/location/search/?lattlong=50.068,-5.316',
        
        ResponseFields:
            title, location_type, latt_long, woeid, distance
    """

    log = cl.customLogger(logging.DEBUG)

    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.Smoke
    def test_valid_query_value(self, get_location_search_api_url,
                               location_search_query_param):
        """
            Test to verify if location details received is as per expected result
                for metaweather api Location Search, on passing a valid city name.
        """
        self.log.info(("*" * 40) + " test_valid_query_value " + ("*" * 40))

        # Reading from conftest value for query parameter i.e. city name
        query = location_search_query_param

        # Reading from the JSON validator file
        data_response = readJson("location_search/valid_query_parameter")

        self.log.info("\nExpected Response:\n %s", data_response[query])

        # Getting the response after making GET API call
        response = ops.get(url=get_location_search_api_url,
                           params={'query': query}
                           )

        self.log.info(
            "\nActual Response:\nResponse Code: %s \nResponse Body: %s",
            response.status_code, response.json())

        allure.dynamic.description(
            "Response time for the request is: " +
            str(response.elapsed.total_seconds()))

        assert response.status_code == requests.codes.ok and \
            response.json() == data_response[query]

    @allure.severity(allure.severity_level.NORMAL)
    def test_valid_query_subset_value(self, get_location_search_api_url,
                                      location_search_query_subset_param):
        """
            Test to verify if location details received is as per expected result
                for metaweather api Location Search, on passing a subset of 
                valid city name.
        """
        self.log.info(
            ("*" * 40) + " test_valid_query_subset_value " + ("*" * 40))

        # Reading from conftest value for query parameter i.e. city name subset
        query = location_search_query_subset_param

        # Reading from the JSON validator file
        data_response = readJson(
            "location_search/valid_subset_query_parameter")

        self.log.info("\nExpected Response:\n %s", data_response[query])

        # Getting the response after making GET API call
        response = ops.get(url=get_location_search_api_url,
                           params={'query': query}
                           )

        self.log.info(
            "\nActual Response:\nResponse Code: %s \nResponse Body: %s",
            response.status_code, response.json())

        allure.dynamic.description(
            "Response time for the request is: " +
            str(response.elapsed.total_seconds()))

        assert response.status_code == requests.codes.ok and \
            response.json() == data_response[query]

    @allure.severity(allure.severity_level.NORMAL)
    def test_valid_random_query_value(self, get_location_search_api_url,
                                      get_random_city):
        """
            Test to verify metaweather api for Location Search on passing a random  
                value in query parameter (city name).
        """
        self.log.info(
            ("*" * 40) + " test_valid_random_query_value " + ("*" * 40))

        # Reading from conftest value for query parameter i.e. city name subset
        query = get_random_city

        self.log.info("Random city selected for test: %s", query)

        # Getting the response after making GET API call
        response = ops.get(url=get_location_search_api_url,
                           params={'query': query}
                           )

        self.log.info(
            "\nActual Response:\nResponse Code: %s \nResponse Body: %s",
            response.status_code, response.json())

        allure.dynamic.description(
            "Response time for the request is: " +
            str(response.elapsed.total_seconds()))

        assert response.status_code == requests.codes.ok

    @allure.severity(allure.severity_level.NORMAL)
    def test_valid_random_lattlong_value(self, get_location_search_api_url,
                                        get_random_latt_long):
        """
            Test to verify metaweather api for Location Search on passing a random  
                value in lattlong parameter (random latitude longitude).
        """
        self.log.info(
            ("*" * 40) + " test_valid_random_lattlong_value " + ("*" * 40))

        # Reading from conftest value for lattlong parameter
        # i.e. latitude & longitude random values
        lattlong = get_random_latt_long

        self.log.info("Random Latitude & Longitude selected for test: %s", lattlong)

        # Getting the response after making GET API call
        response = ops.get(url=get_location_search_api_url,
                           params={'lattlong': lattlong}
                           )

        self.log.info(
            "\nActual Response:\nResponse Code: %s",
            response.status_code)

        allure.dynamic.description(
            "Response time for the request is: " +
            str(response.elapsed.total_seconds()))

        assert response.status_code == requests.codes.ok

    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.Smoke
    def test_valid_lattlong_value(self, get_location_search_api_url,
                                  location_search_lattlong_valid):
        """
            Test to verify if location details received is as per expected result
                for metaweather api Location Search, on passing valid latitudes & longitudes.
        """
        self.log.info(("*" * 40) + " test_valid_lattlong_value " + ("*" * 40))

        # Reading from conftest value for lattlong parameter
        # i.e. latitude & longitude values
        lattlong = location_search_lattlong_valid

        # Reading from the JSON validator file
        data_response = readJson("location_search/valid_lattlong_parameters")

        self.log.info("\nExpected Response:\n %s", data_response[lattlong])

        # Getting the response after making GET API call
        response = ops.get(url=get_location_search_api_url,
                           params={'lattlong': lattlong}
                           )

        self.log.info(
            "\nActual Response:\nResponse Code: %s \nResponse Body: %s",
            response.status_code, response.json())

        allure.dynamic.description(
            "Response time for the request is: " +
            str(response.elapsed.total_seconds()))

        assert response.status_code == requests.codes.ok and \
            response.json() == data_response[lattlong]

    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.Smoke
    @pytest.mark.xfail
    def test_invalid_lattlong_value(self, get_location_search_api_url,
                                    location_search_lattlong_invalid):
        """
            Test to verify if appropriate error is logged when request on metaweather 
                api Location Search, on passing invalid latitudes & longitudes.
        """
        self.log.info(
            ("*" * 40) + " test_invalid_lattlong_value " + ("*" * 40))

        # Reading from conftest value for lattlong parameter
        # i.e. latitude & longitude values
        lattlong = location_search_lattlong_invalid

        # Getting the response after making GET API call
        response = ops.get(url=get_location_search_api_url,
                           params={'lattlong': lattlong}
                           )

        self.log.info(
            "\nActual Response:\nResponse Code: %s", response.status_code)

        allure.dynamic.description(
            "Response time for the request is: " +
            str(response.elapsed.total_seconds()))

        assert response.status_code == requests.codes.BAD_REQUEST

    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.Smoke
    def test_invalid_method_type(self, get_location_search_api_url,
                                 location_search_lattlong_valid):
        """
            Test to verify if appropriate error is logged when request on metaweather 
                api Location Search is made with invalid method type
        """
        self.log.info(("*" * 40) + " test_invalid_method_type " + ("*" * 40))

        # Reading from conftest value for lattlong parameter
        # i.e. latitude & longitude values
        lattlong = location_search_lattlong_valid

        # Getting the response after making POST API call
        response = requests.post(url=get_location_search_api_url,
                                 params={'lattlong': lattlong})

        self.log.info(
            "\nActual Response:\nResponse Code: %s", response.status_code)

        allure.dynamic.description(
            "Response time for the request is: " +
            str(response.elapsed.total_seconds()))

        assert response.status_code == requests.codes.METHOD_NOT_ALLOWED
