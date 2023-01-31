from django.shortcuts import render, redirect
from list_trans.models import Carrier
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.urls import reverse
from .forms import CarrierModelForm

def index(request):
    return render(request, 'index.html')

def all_car(request):
    all_list = Carrier.objects.all()
    context = {'all_list' : all_list}
    return render(request, 'list.html', context)

def detail_car(request, pk):
    try:
        obj = Carrier.objects.get(id=pk)
    except Carrier.DoesNotExist:
        raise Http404
    return render(request, 'list_trans/onecar.html', {'single_obj' : obj})

def delete_car(request, pk):
    try:
        obj = Carrier.objects.get(id=pk)
    except Carrier.DoesNotExist:
        raise Http404
    obj.delete()
    return HttpResponseRedirect(reverse('all_car'))

def create_car(request):
    if request.method == 'POST':
        form = CarrierModelForm(request.POST or None)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.save()
            # return render(request, 'forms.html', {'form':form, 'obj':obj})
            # return redirect(reverse('detail_car', args=[obj.pk]))
            return redirect(f'/allcar/car/{obj.pk}')
    form = CarrierModelForm(request.POST or None)
    return render(request, 'forms.html', {'form':form})

def edit_car(request, pk):
    try:
        obj = Carrier.objects.get(id=pk)
    except Carrier.DoesNotExist:
        raise Http404
    
    if request.method == 'POST':
        form = CarrierModelForm(request.POST, instance=obj)

        if form.is_valid():
            edit_obj = form.save(commit=False)
            edit_obj.save()
    else:
        form = CarrierModelForm(instance=obj)
    
    return render(request, 'edit_car_form.html', {'single_obj': obj, 'form':form})







