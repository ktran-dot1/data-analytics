contact_info = {
    "name": "Kevin Tran",
    "address": "806 marin st",
    "city": "Hayward",
    "state": "CA",
    "zip": "94541"
}

# print results
print(f"""
    {contact_info["name"]}
    {contact_info["address"]}
    {contact_info["city"]}
    {contact_info["state"]}
    {contact_info["zip"]}
"""  )

# remove name
del contact_info["name"]

# create full name dictionary
full_name = {
    "first name": "Kevin",
    "last name": "Tran"
}

# add honorific
full_name.update({
    "honorific": "Mr."
})

# add full name to contact list
contact_info.update({
    "full_name": full_name
})

# print
print(f"""
    {contact_info["full_name"]["honorific"]}
    {contact_info["full_name"]["first name"]}
    {contact_info["full_name"]["last name"]}
    {contact_info["address"]}{contact_info["city"]}
    {contact_info["state"]}{contact_info["zip"]}
""")