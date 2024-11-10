from app import app
import pytest, utility
"""
This file contains a unit test for the update_list feature within the client info page
that switches prescription lists.
"""

def test_update_list():

    c = utility.get_client_by_phone("(123)-456-7890")
    test_data = {
            'id': c[0],
            'active': utility.get_active_prescripts(c),
            'old': utility.get_old_prescripts(c)
    }

    # Load the update page (POST)
    response = app.test_client().post('/update_list', json=test_data)

    # Assert that the response is 200 OK
    assert response.status_code == 200

    # Assert the response JSON contains the expected result
    assert response.json == {'result': c[0]}