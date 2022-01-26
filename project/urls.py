from django.urls import path
from .views import home, project_list


urlpatterns=[
	path('', home, name='home'),
	path('projects/',project_list, name='project_list' )
]