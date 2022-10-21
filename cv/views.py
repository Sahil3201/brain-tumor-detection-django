from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.list import ListView

from .model import ModelDeployment
from .forms import *
from .models import BrainScans
from . import imageClassifier

# def index(request):
#     return HttpResponse("<h1>Hello, world. You're at the cv index.</h1><h3>Try to use paths:<br>- /predict</h3>")

def getPredictions(request):
    if request.method == 'POST':
        form = BrainScansForm(request.POST, request.FILES)

        if form.is_valid():
            # return HttpResponse(ModelDeployment.get_prediction_from_image("cv/model/images/image.jpeg"))
            # return HttpResponse(ModelDeployment.get_prediction_from_image_upload(request.FILES["brain_scan_img"]))
            print("request.FILES['brain_scan_img']")
            print(request.FILES['brain_scan_img'])
            print(request.FILES)
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

def getPredictionsNew(request):
    last_prediction = BrainScans.objects.last()
    if last_prediction and last_prediction.imageName:
        last_prediction.imageName = last_prediction.imageName[:20]

    if request.method == 'POST':
        form = BrainScansFormNew(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            filename = form.instance.image.file.name
            prediction, imageName, original_image = ModelDeployment.get_prediction_from_image_upload_new(form.instance.image.file.name)
            form.instance.prediction = round(prediction*100,2)
            form.instance.imageName = str(request.FILES['image']) #filename
            form.save()

            form = BrainScansFormNew()
            return render(request, 'brain_scan_predict-new.html',
            {'form' : form,
            "prediction": round(prediction*100,2),
            "imageName": str(request.FILES['image']), # str(filename),
            'original_image': original_image.decode('utf-8'),
            "last_prediction": last_prediction}
            )
    else:
        form = BrainScansFormNew()
        return render(request, 'brain_scan_predict-new.html',
        {'form' : form,
            "last_prediction": last_prediction})

class BrainScansListView(ListView):

    model = BrainScans
    paginate_by = 100  # if pagination is desired

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['predict_page'] = timezone.now()
    #     return context

def getPredictionsNewWithImgClassifier(request):
    last_prediction = BrainScans.objects.last()
    if last_prediction and last_prediction.imageName:
        last_prediction.imageName = last_prediction.imageName[:20]

    if request.method == 'POST':
        form = BrainScansFormNew(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            # filename = form.instance.image.file.name

            isMri = imageClassifier.get_class_of_image(form.instance.image.file.name)
            print("isMri!!!!!!!!!!!!!!!!!!!")
            print(isMri)
            prediction, imageName, original_image = ModelDeployment.get_prediction_from_image_upload_new(form.instance.image.file.name)
            form.instance.prediction = round(prediction*100,2)
            form.instance.imageName = str(request.FILES['image']) #filename
            if isMri:
                form.save()
            else:
                prediction = False
                form.instance.delete()

            form = BrainScansFormNew()
            return render(request, 'brain_scan_predict-new-with-MRI-classifier.html',
            {'form' : form,
            "prediction": round(prediction*100,2),
            "imageName": str(request.FILES['image']), # str(filename),
            'original_image': original_image.decode('utf-8'),
            'isNotMri': not isMri,
            "last_prediction": last_prediction}
            )
    else:
        form = BrainScansFormNew()
        return render(request, 'brain_scan_predict-new-with-MRI-classifier.html',
        {'form' : form,
            "last_prediction": last_prediction})
