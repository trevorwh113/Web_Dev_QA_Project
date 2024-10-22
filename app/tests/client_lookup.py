import pytest
import utility

@pytest.fixture
def types():
    """Defines basic data types for comparisons."""
    return {"STR": type(""),
            "INT": type(0),
            "LST": type([])}

def test_get_all_clients(types):
    """
    Success case: Tests that get_all_clients() returns a non-empty
    2d-list matching: [[str, str, str, int], ...]
    """
    data = utility.get_all_clients()
    # Check the ouside list.
    assert type(data) == types["LST"], "Return value should be a list"
    assert len(data) > 0, "Return value should be non-empty"
    # Check the inside list.
    entry = data[0]
    assert type(entry) == types["LST"], "Entry values should be lists"
    assert len(entry) == 4, "Entry values should have 4 elements"
    # Check the values ofthe inside list.
    assert type(entry[0]) == types["STR"], "full_name should be a string"
    assert type(entry[1]) == types["STR"], "birth_date should be a string"
    assert type(entry[2]) == types["STR"], "phone_number should be a string"
    assert type(entry[3]) == types["INT"], "active_prescriptions should be an integer"
