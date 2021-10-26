from django.shortcuts import render
from firebaseConfig import database

# Create your views here.
def getDestinations():
    return database.child("Destinations").get().val()

def getResorts():
  return database.child("Resorts").get().val()


def index(request, template="manageResorts.html"):
  return render(request, template, {"Resorts": getResorts,"Destinations" : getDestinations})

def addNewResort(request):
  tempRest = database.child("Resorts").get().val()
  tempDID = request.POST["restDestId"]

  database.child("Resorts").child(len(tempRest)).set({
    "City":request.POST["restCity"],
    "BasePrice":int(request.POST["restBasePrice"]),
    "Address" : request.POST["restAddress"],
    "Description" : request.POST["restDescription"],
    "DestinationId" : int(tempDID),
    "Image" : "https://thumbs.dreamstime.com/z/resorts-orange-color-word-text-logo-icon-suitable-card-typography-design-127994353.jpg",
    "IsAvailable" : request.POST["restIsAvail"],
    "IsMeal" : request.POST["restIsMeal"],
    "Name" : request.POST["restName"],
    "ResortId" : len(tempRest)
  })
  return render(request, "manageResorts.html", {"Resorts": getResorts,"Destinations" : getDestinations} )
