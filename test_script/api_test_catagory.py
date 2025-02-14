import pytest
import requests

# Base API URL
BASE_URL = "https://api.tmsandbox.co.nz"


@pytest.fixture(scope="module")
def api_response():
    """
    Fixture to execute the API request once per test session
    and return the JSON response.
    """
    end_point = "/v1/Categories/6327/Details.json?catalogue=false"

    # Make API request
    response = requests.get(f"{BASE_URL}/{end_point}")

    # Validate HTTP response status
    assert response.status_code == 200, f"API call failed with status {response.status_code}"

    # Return JSON response
    return response.json()


def test_api_categories_validate_attributes(api_response):
    """
    Test to validate key attributes in the API response.
    """

    # Expected values for validation
    expected_name = "Carbon credits"
    expected_can_relist = True
    expected_promotion_description = "Good position in category"

    # Validate the 'Name' field
    assert api_response["Name"] == expected_name, f"Expected '{expected_name}', got '{api_response['Name']}'"

    # Validate 'CanRelist' field
    assert api_response[
               "CanRelist"] is expected_can_relist, f"Expected '{expected_can_relist}', got '{api_response['CanRelist']}'"

    # Find the "Gallery" promotion in the Promotions list
    gallery_promotion = next((p for p in api_response["Promotions"] if p["Name"] == "Gallery"), None)

    # Ensure the promotion exists before checking its description
    assert gallery_promotion is not None, "Gallery promotion not found in response"

    # Validate the promotion's description
    assert expected_promotion_description in gallery_promotion["Description"], \
        f"Expected description to contain '{expected_promotion_description}', got '{gallery_promotion['Description']}'"