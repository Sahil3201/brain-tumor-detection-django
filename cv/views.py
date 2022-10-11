from django.shortcuts import render
from django.http import HttpResponse
from .model import ModelDeployment
from .forms import *

def index(request):
    return HttpResponse("<h1>Hello, world. You're at the cv index.</h1><h3>Try to use paths:<br>- /predict</h3>")

def getPredictions(request):
    if request.method == 'POST':
        form = BrainScansForm(request.POST, request.FILES)

        if form.is_valid():
            # return HttpResponse(ModelDeployment.get_prediction_from_image("cv/model/images/image.jpeg"))
            # return HttpResponse(ModelDeployment.get_prediction_from_image_upload(request.FILES["brain_scan_img"]))
            print("request.FILES['brain_scan_img']")
            print(request.FILES['brain_scan_img'])
            prediction, imageName, original_image = ModelDeployment.get_prediction_from_image_upload(request.FILES["brain_scan_img"])

            form = BrainScansForm()
            return render(request, 'brain_scan_predict.html',
            {'form' : form,
            "prediction": round(prediction*100,2),
            "imageName": imageName,
            'original_image': original_image.decode('utf-8')}
            )
    else:
        form = BrainScansForm()
        return render(request, 'brain_scan_predict.html', {'form' : form})
