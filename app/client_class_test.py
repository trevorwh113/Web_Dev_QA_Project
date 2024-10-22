
# import utility
from client import Client

import pytest

class TestClient:
    def setup_method(self):
        """Set up a new Client object for each test."""
        self.client = Client('John', 'Doe', '123-456-7890', '01-01-1980')

    def test_init(self):
        """Test the constructor and initial attributes."""
        assert self.client.first_name == 'John'
        assert self.client.last_name == 'Doe'
        assert self.client.phone_number == '123-456-7890'
        assert self.client.dob == '01-01-1980'
        assert self.client.active_prescripts == []
        assert self.client.old_prescripts == []

    def test_add_new_prescript(self):
        """
        GIVEN a client with an empty list of active prescriptions
        WHEN add_new_prescription is called
        THEN a prescription matching the one created appears in that
        clients active prescription array

        """
        prescription = ["Drug Name", 904954, "2024-10-18", "Dr. John Smith", 1]
        self.client.add_new_prescript(prescription)
        assert prescription in self.client.active_prescripts
        assert len(self.client.active_prescripts) == 1



    def test_add_old_prescript(self):
        """
        GIVEN a client with an empty list of active prescriptions
        WHEN add_new_prescription is called
        THEN a prescription matching the one created appears in that
        clients active prescription array

        """
        prescription = ["Drug Name", 904954, "2024-10-18", "Dr. John Smith", 1]
        self.client.add_old_prescript(prescription)
        assert prescription in self.client.old_prescripts
        assert len(self.client.old_prescripts) == 1

        
"""
What I have to test:

utility.py:
- get_active_prescripts()
- get_client_by_phone()
    - should take a string formatted to (xxx)-xxx-xxxx
    - can just strip and convert to each chara to int (count of 10)

client.py:
- init
- add new prescript
- add old prescript

client_info.js
- 

ViewPrescriptions (A1)
ChangePrescriptionStatus (A1)

- Functional test for naviguating to client info page


"""