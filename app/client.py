class Client:
    """
    A class to represent a client.

    Attributes:
    ----------
    first_name : str
        The first name of the client.
    last_name : str
        The last name of the client.
    phone_number : str
        The client's phone number.
    dob : str
        The client's date of birth.
    active_prescripts : list
        A list to hold the client's active prescriptions.
    old_prescripts : list
        A list to hold the client's old prescriptions.
    """
    def __init__(self, first_name, last_name, phone_number, dob):
        self.first_name = first_name
        self.last_name = last_name
        self.phone_number = phone_number
        self.dob = dob
        self.active_prescripts = []
        self.old_prescripts = []
    
    def add_new_prescript(self, prescript):
        
        self.active_prescripts.append(prescript)

    def add_old_prescript(self, prescript):
        self.old_prescripts.append(prescript)
    
    def deactivate_prescript(self, prescript):
        if prescript in self.active_prescripts:
            self.active_prescripts.pop(prescript)
            self.old_prescripts.append(prescript)

    def reactivate_prescript(self, prescript):
        if prescript in self.old_prescripts:
            self.old_prescripts.pop(prescript)
            self.active_prescripts.append(prescript)