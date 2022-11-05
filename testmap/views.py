from django.shortcuts import render
import csv 
import pandas as pd
from testmap.models import IKSAN

with open('C:\\Users\\PC\\Django_study\\mysite\\mysite\\static\\IKSAN_Data.csv') as f:
    dr = csv.DictReader(f)
    s = pd.DataFrame(dr)
ss = []

for i in range(len(s)):
    st = (s['Title'][i], s['Range'][i], s['Lat'][i], s['Lon'][i])
    ss.append(st)
for i in range(len(s)):
    IKSAN.objects.create(Title=ss[i][0], Range=ss[i][1], Lat = ss[i][2], Lon = ss[i][3])


# IKSAN = []
# with open('mysite\static\IKSAN_Data.csv') as csvfile:
#     lines = csv.reader(csvfile, delimiter=',')
#     for i in lines:
#         IKSAN.append(i)

# IKSAN_data = IKSAN[1:]

def index(request):
    return render(request, 'testmap/index.html', {'IKSAN' : IKSAN})