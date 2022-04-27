from django.shortcuts import render, redirect
from .forms import ImovelForm
from .models import Imovel

# Create your views here.
def imovel_list(request):
	context = {'imovel_list':Imovel.objects.all()}
	return render(request, "imovel_register/imovel_list.html", context)

def imovel_form(request, id=0):
	if request.method == "GET":
		if id==0:
			form = ImovelForm()
		else:
			imovel = Imovel.objects.get(pk=id)
			form = ImovelForm(instance=imovel)
		return render(request, "imovel_register/imovel_form.html", {'form':form})
	else:
		if id == 0:
			form = ImovelForm(request.POST)
		else:
			imovel = Imovel.objects.get(pk=id)
			form = ImovelForm(request.POST, instance=imovel)
		if form.is_valid():
			form.save()
		return redirect('/imovel/list')

def imovel_delete(request, id):
	imovel = Imovel.objects.get(pk=id)
	imovel.delete()
	return redirect('/imovel/list')