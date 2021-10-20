from django.shortcuts import render
from firebaseConfig import database

def index(request, template="homepage.html"):
    id = database.child("Users").child("0").child("UserId").get().val()
    firstName = database.child("Users").child("0").child("FirstName").get().val()
    lastName = database.child("Users").child("0").child("LastName").get().val()
    email = database.child("Users").child("0").child("Email").get().val()
    mobile = database.child("Users").child("0").child("Mobile").get().val()
    role = database.child("Users").child("0").child("Role").get().val()

    data = {
        "id": id,
        "firstName": firstName,
        "lastName": lastName,
        "email": email,
        "mobile": mobile,
        "role": role,
    }

    return render(request, template, data)
