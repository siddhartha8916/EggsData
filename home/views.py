from django.shortcuts import render
from .models import *
from .forms import *
import numpy as np
import csv

# Create your views here.
def index(request):
    if request.method == "POST":
        form = CSVForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            obj = Csvs.objects.get(activated=False)
            with open(obj.filename.path,'r') as f:
                reader = csv.reader(f)
                for i,row in enumerate(reader):
                    if i==0:
                        pass
                    else:
                        market = row[0]
                        arrival_date = row[1]
                        price = row[2] if row[2] else 0
                        egg_monthly_price.objects.create(
                            market = market,
                            arrival_date=arrival_date,
                            price=price
                        )
                obj.activated=True
    form = CSVForm()
    context = {'form':form}
    return render(request,'index.html',context)