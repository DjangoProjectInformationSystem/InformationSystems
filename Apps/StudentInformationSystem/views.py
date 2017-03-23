from django.shortcuts import render,redirect
from StudentInformationSystem.forms import *
from StudentInformationSystem.models import *
from django.http import HttpResponse

def index(request):
	return render(request, 'StudentInformationSystem/index.html')


def base(request):
    if request.method == "POST":
        form = PersonalInfoForm(request.POST)
        if form.is_valid():
            PersonInfo = form.save(commit=False)
            PersonInfo.save()
            return redirect('success')
    else:
        form = PersonalInfoForm()
    return render(request, 'StudentInformationSystem/base.html', {'form': form})

	
def acedamicInfo(request):
	if request.method == "POST":
		form = AcedamicInfoForm(request.POST)
		if form.is_valid():
			AcedamicInfo = form.save(commit=False)
			AcedamicInfo.save()
			return redirect('success')
	else:
		form = AcedamicInfoForm()
	return render(request, 'StudentInformationSystem/success.html', {'form': form})

def additionalInfo(request):
	if request.method == "POST":
		form = AdditionalInfoForm(request.POST)
		if form.is_valid():
			AdditionalInfo = form.save(commit=False)
			AdditionalInfo.save()
			return redirect('success')
	else:
		form = AdditionalInfoForm()
	return render(request, 'StudentInformationSystem/additionalInfo.html', {'form': form})
