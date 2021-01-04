import requests
import json
import logging
import utilities.custom_logger as cl

from http import HTTPStatus


log = cl.customLogger(logging.DEBUG)


def get(**kwargs):

    """
        Method to generate an API request to URL received 
            from the Test Case along with the parameters.
    """
    url = kwargs.get('url', None)
    params = kwargs.get('params', None)
    woeid = kwargs.get('woeid', None)
    date = kwargs.get('date', None)

    try:
        if not params:
            if not date:
                endpoint = f"{url}/{woeid}"
                response = requests.get(url=endpoint)

            else:
                endpoint = f"{url}/{woeid}/{date}"
                response = requests.get(url=endpoint)

        elif not woeid:
            response = requests.get(url=url, params=params)

        return response

    except Exception as Argument:
        log.error(
            "Exception occured in GET API call with details %s", Argument)
