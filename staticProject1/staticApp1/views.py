from django.shortcuts import render
def view1(request):
    myName="Tejodeep"
    favActor="Ranbir"
    favCar="ferrari"
    favAnimal="german-shepherd"
    d={'name':myName,'actor':favActor,'car':favCar,'animal':favAnimal}
    return render(request,'templateApp1/s1.html',d)
# Create your views here.
