# Global list (Outside of the class)
cust_list = []


class RewardsProgram:
    '''For customer's reward information'''

    def __init__(self, cust_name, phone, email):
        self.name = cust_name
        self.phone = phone
        self.email = email

    def profile(self):
       print(f"Name: {self.name}")
       print(f"Phone: {self.phone}")
       print(f"Email: {self.email}")

    def thank_you(self):
        return f"Thank you, {self.name}, for visiting our restaurant"
    
    def add_cust_list(self):
        cust_info = (self.name, self.phone, self.email)
        cust_list.append(cust_info)

# create three instance
cust1 = RewardsProgram("John Doe", "510-135-2468", "jdoe@mail.com")
cust2 = RewardsProgram("Sam Pike", "510-987-1234", "spike@mail.com")
cust3 = RewardsProgram("Stewy Griffin", "808-725-9017", "sgriff@mail.com")

# Call
cust1.profile()
cust1.thank_you()
cust1.add_cust_list()

cust2.profile()
cust2.thank_you()
cust2.add_cust_list()

cust3.profile()
cust3.thank_you()
cust3.add_cust_list()

# print
print(cust_list)
