from django.shortcuts import render
from firebaseConfig import database

# Create your views here.
def getDestinations():
  return database.child("Destinations").get().val()

def index(request, template="manageDestinations.html"):
  return render(request, template, {"Destinations": getDestinations})

def addNewDestinations(request):
  tempDest = database.child("Destinations").get().val()

  dname = request.POST["destName"]
  daddress = request.POST["destCity"]
  dcity = request.POST["destCity"]
  ddescription = request.POST["destDescription"]
  did = len(tempDest)
  Image = "https://previews.123rf.com/images/dragomirescu/dragomirescu1808/dragomirescu180800451/105737910-destination-word-hand-writing-text-typography-design-with-black-and-orange-color-suitable-for-logo-b.jpg"

  database.child("Destinations").child(len(tempDest)).set({
    "Address" : daddress,
    "City" : dcity,
    "Description" : ddescription,
    "DestinationId" : did,
    "Image" : Image,
    "Name" : dname
  })
  return render(request, "manageDestinations.html", {"Destinations": getDestinations} )
