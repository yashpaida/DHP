from django.shortcuts import render
from firebaseConfig import database, Destination, Resort, Room

Destinations : Destination  = database.child("Destinations").get().val()
Resorts : Resort = database.child("Resorts").get().val()
Rooms : Room = database.child("Rooms").get().val()

Filtered_Rooms = []
tempDName = ""

def index(request, template="homepage.html"):
    print(Destinations)
    return render(request, template, {"Destinations": Destinations, "Resorts" : Resorts} )

def contactus(request,template="contactus.html"):
    return render(request,template)
    
def Rajasthan(request, template="Rajasthan.html"):
    return render(request, template)

def openpackage(request,id,rid,template="package.html"):
    Filtered_Resorts = [r for r in Resorts if r['DestinationId'] == id]
    Filtered_Rooms = [r for r in Rooms if r['ResortId'] == rid]

    for d in Destinations:
        if (d["DestinationId"] == id):
            tempDName = d["Name"]
    
    return render(request,template,{"DId":id,"DName":tempDName,"Resorts":Filtered_Resorts,"Rooms":Filtered_Rooms})