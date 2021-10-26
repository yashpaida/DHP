from django.shortcuts import render
from firebaseConfig import database

def getUsers():
  return database.child("Users").get().val()

def index(request, template="manageUsers.html"):
  return render(request, template, {"Users": getUsers} )

def addNewUser(request):
  fname = request.POST["fname"]
  lname = request.POST["lname"]
  uid = request.POST["uid"]
  email = request.POST["email"]
  mobileno = request.POST["mobileno"]
  role = request.POST["role"]
  password = "User@123"

  tempUsers = database.child("Users").get().val()
  database.child("Users").child(len(tempUsers)).set({
    "Email" :  email,
    "FirstName" : fname,
    "LastName" : lname,
    "Mobile" : int(mobileno),
    "Password" : password,
    "Role" : role,
    "UserId" : uid
  })
  return render(request, "manageUsers.html", {"Users": getUsers} )

