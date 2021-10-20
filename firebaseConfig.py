import pyrebase

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
database = firebase.database()