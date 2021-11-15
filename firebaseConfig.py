import pyrebase

Destination = {
    "Address" : str,
    "City" : str,
    "Description" : str,
    "DestinationId" : int,
    "Image" : str,
    "Name" : str
}
Package = {
    "Date" : str,
    "DestinationId" : int,
    "NoOfDay" : int,
    "NoOfMember" : int,
    "PackageId" : int,
    "Price" : int,
    "ResortId" : int,
    "RoomIds" : list(),
    "UserId" : str
}
Resort = {
    "Address" : str,
    "Description" : str,
    "DestinationId" : int,
    "Images" : list(),
    "IsAvailable" : str,
    "IsMeal" : str,
    "Name" : str,
    "ResortId" : int,
    "City":str
}
Room = {
    "AC" : str,
    "Description" : str,
    "Images" : list(),
    "Price" : int,
    "ResortId" : int,
    "RoomId" : int,
    "Type" : str
}
User = {
    "Email" : str,
    "FirstName" : str,
    "LastName" : str,
    "Mobile" : int,
    "Password" : str,
    "Role" : str,
    "UserId" : str
}

class Database(): 
    Destinations : list(Destination)
    Package : list(Package)
    Resorts : list(Resort)
    Room : list(Room)
    User :list(User)

class CurrentUser():
    Email = None
    FirstName = None
    LastName = None
    Mobile = None
    Password = None
    Role = None
    UserId = None


config = {
    "apiKey": "AIzaSyCbEdFDC81kMdg9f5_mdERirEn1ZkN4aFE",
    "authDomain": "divineholidaypackage.firebaseapp.com",
    "databaseURL": "https://divineholidaypackage-default-rtdb.firebaseio.com",
    "projectId": "divineholidaypackage",
    "storageBucket": "divineholidaypackage.appspot.com",
    "messagingSenderId": "385119113706",
    "appId": "1:385119113706:web:b9f4b7a7346438d1a4a293",
}
firebase = pyrebase.initialize_app(config)
authe = firebase.auth()
database : Database  = firebase.database()
