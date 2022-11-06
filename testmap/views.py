from django.shortcuts import render
import csv 
import pandas as pd
from testmap.models import IKSAN
from . import models


## DB에 IKSAN_DATA.csv 읽어서 저장하기
with open('C:\\Users\\PC\\Django_study\\mysite\\mysite\\static\\IKSAN_Data.csv') as f:
    dr = csv.DictReader(f)
    s = pd.DataFrame(dr)
ss = []

for i in range(len(s)):
    st = (s['Title'][i], s['Range'][i], s['Lat'][i], s['Lon'][i])
    ss.append(st)
for i in range(len(s)):
    IKSAN.objects.create(Title=ss[i][0], Range=ss[i][1], Lat = ss[i][2], Lon = ss[i][3])

def index(request):
    IKSAN_DATA = models.IKSAN.objects.all()
    return render(request, 'testmap/index.html', {'IKSAN_DATA' : IKSAN_DATA})