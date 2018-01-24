from django.shortcuts import render
from .forms import addcomputerForm
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Computer

#from django.db.models import Q
# Create your views here.
def home(request):
	context = locals()
	template = 'home.html'
	return render(request, template, context)


def addcomputer(request):
	# form = addcomputerForm( request.POST or None)

	# if form.is_valid():
	# 	print(request.POST)

	# context = locals()
	# template = 'addcomputer.html'
	# return render(request, template, context)
	if request.POST:
		form = addcomputerForm(request.POST)
		if form.is_valid():
			form.save()

			return HttpResponseRedirect(reverse('addsuccess'))
	else:
		form = addcomputerForm()

	args={}
	
	args['form']=form
	return render(request,'addcomputer.html',args)

def viewcomputer(request):
	form = addcomputerForm()
	posts = Computer.objects.all()
	
	args = {'form': form, 'posts': posts}
	template = 'viewcomputer.html'
	return render(request, template, args)

def addsuccess(request):
	template= 'addsuccess.html'
	return render(request,template)


# query=request.GET.get("q")
# if query:
# 	queryset_list= queryset_list.filter(
# 		Q(ip_address__icontains=query)
# 		)