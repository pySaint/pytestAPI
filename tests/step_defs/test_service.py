import pytest
import requests

from pytest_bdd import scenarios, given, then, parsers


# Shared Variables

DUCKDUCKGO_API = 'https://api.duckduckgo.com/'


# Scenarios

scenarios('../features/service.feature')


# Given Steps
@pytest.fixture
@given(parsers.parse('the DuckDuckGo API is queried with "{phrase}"'))
def ddg_response(phrase):
    params = {'q': phrase, 'format': 'json'}
    response = requests.get(DUCKDUCKGO_API, params=params)
    return response


# Then Steps
@then(parsers.parse('the response contains results for "{phrase}"'))
def ddg_response_contents(ddg_response, phrase):
    assert phrase.lower() == ddg_response.json()['Heading'].lower()


@then(parsers.parse('the response status code is "{code:d}"'))
def ddg_response_code(ddg_response, code):
    assert ddg_response.status_code == code
