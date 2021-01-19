from django.shortcuts import render
from django.contrib import messages

# Create your views here.
from .models import Contact_sodesh, Contact_from_compnay
from .models import Contact_NewDhakaCity, Contact_Swadesh,Contact_RiverParkModelTown
from django.shortcuts import render, redirect
def sodesh_contact(request):
    try:
        if request.method == 'POST':
            username = request.POST.get('username')
            company_name = request.POST.get('company_name')
            plot_number = request.POST.get('plot_number')
            email = request.POST.get('email')
            contact_number = request.POST.get('contact_number')
            contact_sodesh = Contact_sodesh(username=username,company_name =company_name,plot_number = plot_number,email=email,contact_number=contact_number, user_id=request.user)
            contact_sodesh.save()
            messages.success(request,'contact post send successfully and your profile varify soon')
            return redirect('/home')
    except:
        messages.success(request,'please register first')
        return redirect('/home')

    return render(request,'contact_sodesh.html')
# new swadesh city part
def swadesh_contact(request):
    try:
        if request.method == 'POST':
            username = request.POST.get('username')
            company_name = request.POST.get('company_name')
            plot_number = request.POST.get('plot_number')
            email = request.POST.get('email')
            contact_number = request.POST.get('contact_number')
            contact_swadesh= Contact_Swadesh(username=username,company_name =company_name,plot_number = plot_number,email=email,contact_number=contact_number, user_id=request.user)
            contact_swadesh.save()
            messages.success(request,'contact post send successfully and your profile varify soon')
            return redirect('/public_swadesh')
    except:
        messages.success(request,'please register first')
        return redirect('/public_swadesh')

    return render(request,'contact_swadesh.html')

# new dhaka city part
def newDhakaCity_contact(request):
    try:
        if request.method == 'POST':
            username = request.POST.get('username')
            company_name = request.POST.get('company_name')
            plot_number = request.POST.get('plot_number')
            email = request.POST.get('email')
            contact_number = request.POST.get('contact_number')
            contact_NewDhakaCity= Contact_NewDhakaCity(username=username,company_name =company_name,plot_number = plot_number,email=email,contact_number=contact_number, user_id=request.user)
            contact_NewDhakaCity.save()
            messages.success(request,'contact post send successfully and your profile varify soon')
            return redirect('/public_new_dhaka_city')
    except:
        messages.success(request,'please register first')
        return redirect('/public_new_dhaka_city')

    return render(request,'contact_newDhakaCity.html')
# river park model town part
def riverParkModelTown_contact(request):
    try:
        if request.method == 'POST':
            username = request.POST.get('username')
            company_name = request.POST.get('company_name')
            plot_number = request.POST.get('plot_number')
            email = request.POST.get('email')
            contact_number = request.POST.get('contact_number')
            contact_RiverParkModelTown= Contact_RiverParkModelTown(username=username,company_name =company_name,plot_number = plot_number,email=email,contact_number=contact_number, user_id=request.user)
            contact_RiverParkModelTown.save()
            messages.success(request,'contact post send successfully and your profile varify soon')
            return redirect('/public_river_park_model_town')
    except:
        messages.success(request,'please register first')
        return redirect('/public_river_park_model_town')

    return render(request,'contact_river_park_model_town.html')

def company_contact_to_admin(request):
    try:
        if request.method == 'POST':
            username = request.POST.get('username')
            company_name = request.POST.get('company_name')
            package_name = request.POST.get('package_name')
            email = request.POST.get('email')
            contact_number = request.POST.get('contact_number')
            contact_from_compnay = Contact_from_compnay(username=username,company_name =company_name,package_name = package_name,email=email,contact_number=contact_number)
            contact_from_compnay.save()
            messages.success(request,'your post send to Admin and inform you as soon as possible')
            return redirect('/pricing')
    except:
        messages.success(request,'please register first')
        return redirect('/')

    return render(request,'contact_from_company.html')
