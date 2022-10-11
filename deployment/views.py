from django.http import HttpResponse
from django.shortcuts import render

def classification(request):
    if request.method == 'POST' and request.FILES['myfile']:
        
        myfile = request.FILES['myfile']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        img_file = fs.url(filename)
        
        pred = "" #TODO make prediction
        return render(request, 'cv/classification.html', {'original_img': img_file,
                                                            'prediction': pred})
        
    return render(request, 'cv/classification.html') 


def index(request):
    return HttpResponse("<h1>Welcome to the django computer vision deployment!</h1><h3>Try using paths:<br>- /admin<br>- /cv</h3>")
