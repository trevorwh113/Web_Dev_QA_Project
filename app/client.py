class Client:
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