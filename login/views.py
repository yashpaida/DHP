from django.shortcuts import render, redirect
from firebaseConfig import database,CurrentUser,User

# Create your views here.

def getUsers():
  return database.child("Users").get().val()

def index(request, template="login.html"):
    return render(request, template)

def loginUser(request):
  email = request.POST["loginEmail"]
  password = request.POST["loginPassword"]

  for i in getUsers():
    if(i["Email"] == email and i["Password"] == password):
        CurrentUser.Email = i["Email"]
        CurrentUser.FirstName = i["FirstName"]
        CurrentUser.LastName = i["LastName"]
        CurrentUser.Mobile = i["Mobile"]
        CurrentUser.Password = i["Password"]
        CurrentUser.Role = i["Role"]
        CurrentUser.UserId = i["UserId"]

        Destinations  = database.child("Destinations").get().val()
        Resorts = database.child("Resorts").get().val()

        print(CurrentUser.Role)
        
        return redirect(request, "/", {"Destinations": Destinations, "Resorts" : Resorts} )
        
    else:
        print("Invalid Login")

def signupUser(request):
  fname = request.POST["signupFName"]
  lname = request.POST["signupLName"]
  uid = len(getUsers)
  email = request.POST["signupEmail"]
  mobileno = request.POST["signupMobileNo"]
  role = "User"
  password = request.POST["signupPassword"]

  for i in getUsers():
    if(i["Email"] != email):
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
    else:
      print("Already Registered")
  return redirect(request, "login", {"Users": getUsers} )