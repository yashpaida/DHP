from django.shortcuts import render
from firebaseConfig import database, Destination, Resort

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

    Destinations : Destination  = database.child("Destinations").get().val()
    Resorts : Resort = database.child("Resorts").get().val()

    return render(request, template, {"Destinations": Destinations, "Resorts" : Resorts} )
