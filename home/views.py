from django.shortcuts import render, HttpResponse
import pyrebase

config = {
    "apiKey": "AIzaSyBbqBYyQupIFIErFjivBq4mRN1cd04xl3Q",
  "authDomain": "levelmonitoring-81d6a.firebaseapp.com",
  "databaseURL": "https://levelmonitoring-81d6a-default-rtdb.asia-southeast1.firebasedatabase.app",
  "projectId": "levelmonitoring-81d6a",
  "storageBucket": "levelmonitoring-81d6a.appspot.com",
  "messagingSenderId": "950560275886",
  "appId": "1:950560275886:web:f720bcc9574a11c035dc3f",
  "measurementId": "G-D3HRY2D52D"
}

firebase = pyrebase.initialize_app(config)
authe = firebase.auth()
database = firebase.database()
# Create your views here.

def index(request):
    datalevel = database.child('S1').get().val()
    context = {
        'level1' : datalevel
    }
    return render(request, 'index.html', context)
    # For displaying model data or database data 
    
    # return HttpResponse("This is Home Page")

def about(request):
    return render(request, 'about.html')
    # return HttpResponse("This is About Page")