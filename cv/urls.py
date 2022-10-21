from django.urls import path
from . import views

urlpatterns = [
    # path('', views.index, name='index'),
    path('predict/', views.getPredictions, name='prediction'),
    path('predict-new/', views.getPredictionsNew, name='predictionNew'),
    path('predict-new-with-img-classifier/', views.getPredictionsNewWithImgClassifier, 
        name='predictionNewWithImgClassifier'),
    path('', views.getPredictionsNewWithImgClassifier, 
        name='predictionHome'),
    path('history/', views.BrainScansListView.as_view(), name='history'),
]
