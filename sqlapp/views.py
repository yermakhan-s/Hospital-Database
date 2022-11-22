from django.http import HttpResponseRedirect, HttpResponseNotFound
from django.shortcuts import render
from .models import *
# Create your views here.
def disease_type(request):
    diseasetype = DiseaseType.objects.all()
    return render(request, "sqlapp/disease_type/disease_type.html", {"diseasetype": diseasetype})
def create_disease_type(request):
    if request.method == "POST":
        diseasetype = DiseaseType()
        diseasetype.id = request.POST.get("ID")
        diseasetype.description = request.POST.get("description")
        diseasetype.save()
    return HttpResponseRedirect("/sqlapp/disease_type/")
def edit_disease_type(request, id):
    try:
        diseasetype = DiseaseType.objects.get(id=id)

        if request.method == "POST":
            diseasetype.id = request.POST.get("ID")
            diseasetype.description = request.POST.get("description")
            diseasetype.save()
            return HttpResponseRedirect("/sqlapp/disease_type/")
        else:
            return render(request, "sqlapp/disease_type/edit_disease_type.html", {"diseasetype": diseasetype})
    except DiseaseType.DoesNotExist:
        return HttpResponseNotFound("<h2>Disease-type not found</h2>")
def delete_disease_type(request, id):
    try:
        diseasetype = DiseaseType.objects.get(id=id)
        diseasetype.delete()
        return HttpResponseRedirect("/sqlapp/disease_type/")
    except DiseaseType.DoesNotExist:
        return HttpResponseNotFound("<h2>Disease-type not found</h2>")

def country(request):
    country = Country.objects.all()
    return render(request, "sqlapp/country/country.html", {"country": country})
def disease(request):
    disease = Disease.objects.all()
    return render(request, "sqlapp/disease/disease.html", {"disease": disease})
def discover(request):
    discover = Discover.objects.all()
    return render(request, "sqlapp/discover/discover.html", {"discover": discover})
def users(request):
    users = Users.objects.all()
    return render(request, "sqlapp/users/users.html", {"users": users})
def public_servant(request):
    pub = PublicServant.objects.all()
    return render(request, "sqlapp/public_servant/public_servant.html", {"pub": pub})
def doctor(request):
    doctor = Doctor.objects.all()
    return render(request, "sqlapp/doctor/doctor.html", {"doctor": doctor})
def specialize(request):
    spec = Specialize.objects.all()
    return render(request, "sqlapp/specialize/specialize.html", {"spec": spec})
def record(request):
    rec = Record.objects.all()
    return render(request, "sqlapp/record/record.html", {"rec": rec})

