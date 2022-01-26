from django.shortcuts import render
from django.contrib.auth.models import User
from .models import Project, Review,Tag

# Create your views here.
def home(request):
	developers=User.objects.all()
	context={
		'developers':developers
	}
	return render(request, 'home.html',context)

def project_list(request):
	projects=Project.objects.all()
	return render(request, 'project_list.html', {'objects':projects})

def project_detail(request, pk):
    project=Project.objects.get(id=pk)
    return render(request, 'project_detail.html', {'project':project})
