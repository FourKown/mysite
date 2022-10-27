from django.shortcuts import render
import csv 

IKSAN = []
with open('mysite\static\IKSAN_Data.csv') as csvfile:
    lines = csv.reader(csvfile, delimiter=',')
    for i in lines:
        IKSAN.append(i)

data = IKSAN[1:]

def index(request):
    return render(request, 'testmap/index.html', {'data':data})