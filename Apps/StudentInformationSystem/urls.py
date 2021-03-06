from django.conf.urls import url
from StudentInformationSystem import views

urlpatterns = [ 
	url(r'^EditProfile$',views.editStudent,name = 'EditProfile'),
	url(r'^$',views.index,name = 'index'),
	url(r'^filter$',views.filter,name = 'filter'),
	url(r'^base$',views.base,name = 'base'),
	url(r'^acedamicInfo$',views.acedamicInfo,name = 'acedamicInfo'),
	url(r'^additionalInfo$',views.additionalInfo,name = 'additionalInfo'),
	url(r'^success$',views.success,name = 'success'),
	url(r'^StudentView$',views.viewStudent,name = 'StudentView'),
	url(r'^home$',views.notifications,name = 'notifications'),
	url(r'^resume$',views.resume,name = 'resume'),
	url(r'^edit$',views.edit,name = ''),
	url(r'^TPO$',views.NotificationInfo,name = 'TPO'),
	url(r'^list$',views.list,name = 'list'),
	url(r'^faculty$',views.SuggestionInfo,name = 'faculty'),
	url(r'^fhome$',views.fnotifications,name = 'fhome'),
]