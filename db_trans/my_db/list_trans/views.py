from django.shortcuts import render
from list_trans.models import Сarrier

def start_page(request):
    all_list = Сarrier.objects.all()
    return render(request, 'start_page', {'all_list':all_list})