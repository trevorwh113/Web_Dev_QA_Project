"""
Tests the client class used to transfer certain kinds of 
information about clients. 
"""
from client import Client
import pytest

def test_init():
    """
    GIVEN a new Client object
    WHEN initialized
    THEN all attributes should match those assigned
    """
    client = Client('John', 'Doe', '123-456-7890', '01-01-1980')
    assert client.first_name == 'John'
    assert client.last_name == 'Doe'
    assert client.phone_number == '123-456-7890'
    assert client.dob == '01-01-1980'
    assert client.active_prescripts == []
    assert client.old_prescripts == []

def test_add_new_prescript():
    """
    GIVEN a client with an empty list of active prescriptions
    WHEN add_new_prescription is called
    THEN a prescription matching the one created appears in that
    clients active prescription array
    """
    client = Client('John', 'Doe', '123-456-7890', '01-01-1980')

    prescription = ["Drug Name", 904954, "2024-10-18", "Dr. John Smith", 1]
    client.add_new_prescript(prescription)
    assert prescription in client.active_prescripts
    assert len(client.active_prescripts) == 1

def test_add_old_prescript():
    """
    GIVEN a client with an empty list of old prescriptions
    WHEN add_old_prescription is called
    THEN a prescription matching the one created appears in that
    client's old prescription array
    """
    client = Client('John', 'Doe', '123-456-7890', '01-01-1980')

    prescription = ["Drug Name", 904954, "2024-10-18", "Dr. John Smith", 1]
    client.add_old_prescript(prescription)
    assert prescription in client.old_prescripts
    assert len(client.old_prescripts) == 1