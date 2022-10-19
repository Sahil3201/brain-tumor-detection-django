from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('predict/', views.getPredictions, name='prediction'),
    path('predict-new/', views.getPredictionsNew, name='predictionNew'),
    path('history/', views.BrainScansListView.as_view(), name='history'),
]
