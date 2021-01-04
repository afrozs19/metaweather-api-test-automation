import logging
import pytest
import requests
import allure
import utilities.custom_logger as cl

import resources.operations as ops
from utilities.read_json import readJson


@pytest.mark.LocationDay
class TestLocationDay:
    
    """
        URL:
            '/api/location/(woeid)/(date)/'

        Arguments:
            Below arguments needs to be added in-place.\n
                'woeid' - Where On Earth ID. Docs. 
                'date' - Date in the format yyyy/mm/dd. 
                
        Examples:
            Below are the list of examples.\n
                '/api/location/44418/2013/4/27/' - London on a 27th Apr 2013 
                '/api/location/2487956/2013/4/30/' - San Francisco on 30th April 2013

        ResponseFields:
            Returns a date ordered list of fields as described in 
                the consolidated_weather section of the location method.
    """

    log = cl.customLogger(logging.DEBUG)

    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.Smoke
    def test_valid_woeid_date(self, get_location_api_url,
                               get_valid_date, get_valid_woeid):
        """
            Test to verify if Weather Details are fetched for 
                the passed woeid & date, and if it matches with 
                test data present in json.
        """

        self.log.info(("*" * 40) + " test_valid_woeid_date " + ("*" * 40))

        # Reading from conftest value for woeid & date
        woeid = get_valid_woeid
        date =get_valid_date

        # Reading from the JSON validator file
        data_response = readJson(f"location_day/{woeid}")

        # Getting the response after making GET API call
        response = ops.get(url=get_location_api_url,
                           woeid=woeid,
                           date=date
                           )

        self.log.info(
            "\nActual Response:\nResponse Code: %s",
            response.status_code)

        allure.dynamic.description(
            "Response time for the request is: " +
            str(response.elapsed.total_seconds()))

        assert response.status_code == requests.codes.ok and \
            response.json() == data_response[date]
    
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.Smoke
    @pytest.mark.xfail
    def test_invalid_method_type(self, get_location_api_url,
                                 get_valid_date, get_valid_woeid):
        """
            Test to verify if appropriate error is logged when request on metaweather 
                api Location is made with invalid method type
        """

        self.log.info(("*" * 40) + " test_invalid_method_type " + ("*" * 40))

        # Reading from conftest value for woeid & date
        woeid = get_valid_woeid
        date =get_valid_date

        # Getting the response after making POST API call
        response = requests.post(f"{get_location_api_url}/{woeid}/{date}")

        self.log.info(
            "\nActual Response:\nResponse Code: %s", response.status_code)

        allure.dynamic.description(
            "Response time for the request is: " +
            str(response.elapsed.total_seconds()))

        assert response.status_code == requests.codes.METHOD_NOT_ALLOWED
    
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.Smoke
    def test_valid_random_woeid(self, get_location_api_url,
                                get_location_search_api_url,
                                 get_valid_date, get_random_city,
                                 get_valid_woeid):
        """
            Test to verify if Weather Details are fetched for 
                the passed random woeid & date, and if it matches.
            If: woeid is None (City is not found in Location Search API)
                API response status code is compared with HTTP Status code 404.
            Else: 
                API response status code is compared with HTTP Status code 200
        """

        self.log.info(("*" * 40) + " test_valid_random_woeid " + ("*" * 40))

        # Reading from conftest value for woeid & date
        query = get_random_city
        date = get_valid_date

        self.log.info("Random city selected for test: %s", query)

        # Getting the response from Location Search API
        ls_response = ops.get(url=get_location_search_api_url,
                           params={'query': query}
                           )  
        ls_response = ls_response.json()

        if not ls_response:
            woeid = None
        else:
            woeid = ls_response[0]["woeid"]

            # Getting the response after making GET API call
        response = ops.get(url=get_location_api_url,
                           woeid=woeid,
                           date=date
                           )

        self.log.info(
            "\nActual Response:\nResponse Code: %s",
            response.status_code)

        allure.dynamic.description(
            "Response time for the request is: " +
            str(response.elapsed.total_seconds()))

        if not woeid:
            assert response.status_code == requests.codes.NOT_FOUND
        else:
            assert response.status_code == requests.codes.ok