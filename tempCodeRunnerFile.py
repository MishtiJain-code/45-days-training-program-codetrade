contacts = [

    {
        "name": "Alex",
        "phone": "9876543210",
        "email": "alex@gmail.com"
    },

    {
        "name": "Mishti",
        "phone": "9123456780",
        "email": "mishti@gmail.com"
    },

    {
        "name": "Riya",
        "phone": "9988776655",
        "email": "riya@gmail.com"
    },

    {
        "name": "Rahul",
        "phone": "9871204567",
        "email": "rahul@gmail.com"
    },

    {
        "name": "Aman",
        "phone": "9012345678",
        "email": "aman@gmail.com"
    }
]


def find_contact(name):

    for contact in contacts:

        # case-insensitive comparison
        if contact["name"].lower() == name.lower():

            return contact

    return "Contact not found"


search_name = input("Enter contact name: ")

result = find_contact(search_name)

print(result)