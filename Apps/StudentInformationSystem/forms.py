from django.forms import ModelForm
from django import forms
from StudentInformationSystem.models import *

class PersonalInfoForm(ModelForm):
	class Meta:
		model = PersonalInfo
		fields = '__all__'	
		widgets = {'studentId': forms.HiddenInput()}
	
class NotificationForm(ModelForm):
	class Meta:
		model = Notifications
		fields = '__all__'	
		widgets = {'TPOId': forms.HiddenInput()}
	def __init__(self, *args, **kwargs):
		# first call parent's constructor
		super(NotificationForm, self).__init__(*args, **kwargs)
		# there's a `fields` property now
		self.fields['TPOId'].required = False
		
class SuggestionForm(ModelForm):
	class Meta:
		model = Suggestion
		fields = '__all__'	
		widgets = {'facultyId': forms.HiddenInput(),'studentId':forms.HiddenInput()}
	def __init__(self, *args, **kwargs):
		# first call parent's constructor
		super(SuggestionForm, self).__init__(*args, **kwargs)
		# there's a `fields` property now
		self.fields['facultyId'].required = False
		self.fields['studentId'].required = False

class AcedamicInfoForm(forms.ModelForm):
	class Meta:
		model = AcedamicInfo
		fields = '__all__'
		widgets = {'studentId': forms.HiddenInput()}
		
	def __init__(self, *args, **kwargs):
		# first call parent's constructor
		super(AcedamicInfoForm, self).__init__(*args, **kwargs)
		# there's a `fields` property now
		self.fields['studentId'].required = False
		
class AdditionalInfoForm(ModelForm):
	class Meta:
		model = AdditionalInfo
		fields = '__all__'
		widgets = {'studentId': forms.HiddenInput()}
	def __init__(self, *args, **kwargs):
		# first call parent's constructor
		super(AdditionalInfoForm, self).__init__(*args, **kwargs)
		# there's a `fields` property now
		self.fields['studentId'].required = False
					
