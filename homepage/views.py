from django.shortcuts import render
from firebaseConfig import database, Destination, Resort, Room, CurrentUser

Destinations : Destination  = database.child("Destinations").get().val()
Resorts : Resort = database.child("Resorts").get().val()
Rooms : Room = database.child("Rooms").get().val()

Filtered_Rooms = []
tempDName = ""

def index(request, template="homepage.html"):
    Destinations : Destination  = database.child("Destinations").get().val()
    Resorts : Resort = database.child("Resorts").get().val()
    Rooms : Room = database.child("Rooms").get().val()
    return render(request, template, {"Destinations": Destinations, "Resorts" : Resorts} )

def contactus(request,template="contactus.html"):
    return render(request,template)
    
def Rajasthan(request, template="Rajasthan.html"):
    return render(request, template)

def Invoice(request, template="Invoice.html"):
    package ={
    "Date" : "01/01/2022",
    "DestinationId" : 0,
    "NoOfDay" : 7,
    "NoOfMember" : 5,
    "PackageId" : 0,
    "Price" : 45000,
    "ResortId" : 0,
    "RoomIds" : [ 0, 1, 3 ],
    "UserId" : 0
    }
    return render(request,template,{"Package":package})

def openResorts(request,id,template="Resorts.html"):
    Filtered_Resorts = [r for r in Resorts if r['DestinationId'] == id]

    for d in Destinations:
        if (d["DestinationId"] == id):
            tempDName = d["Name"]
    
    return render(request,template,{"DId":id,"DName":tempDName,"Resorts":Filtered_Resorts})
    
def openRooms(request,id,rid,template="Rooms.html"):
    if CurrentUser.Role != None:
        Filtered_Rooms = [r for r in Rooms if r['ResortId'] == rid]

        return render(request,template,{"DName":tempDName,"Rooms":Filtered_Rooms,"CurrentUser":CurrentUser})
    else:
        return render(request,"login.html")

