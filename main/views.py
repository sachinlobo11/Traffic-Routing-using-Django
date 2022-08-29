from django.shortcuts import render

from django.http import HttpResponse
from urllib.request import urlopen
import json
def index(response):
    if response.method == "POST":
        if response.POST.get("save"):
            url="https://graphhopper.com/api/1/route?point=51.131,12.414&point=48.224,3.867&profile=car&details=country&instructions=true&locale=en&calc_points=true&key=72b4236f-8680-42b0-8883-6938d4f2a811"
            responseData=urlopen(url).read()

            data=json.loads(responseData)

            print(data["paths"][0]["instructions"])

            instructionsLength= len(data["paths"][0]["instructions"])
            text =[]
            street_Data=[]
            print(data["paths"][0]["instructions"][0]["text"])
            print(instructionsLength)
            for a in range(instructionsLength):
                text.append(data["paths"][0]["instructions"][a-1]["text"])
                street_Data.append(data["paths"][0]["instructions"][a-1]["street_name"])
            parseDataFE = {
            "text":text,
            "street_name":street_Data
            }
            print(parseDataFE)
            return render(response,"main/list.html",{"text":text})
            
    
        
# Create your views here.
