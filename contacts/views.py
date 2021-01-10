from django.shortcuts import render
from django.contrib import messages

# Create your views here.
from .models import Contact_sodesh, Contact_from_compnay
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
