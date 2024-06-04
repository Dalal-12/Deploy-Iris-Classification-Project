from django.shortcuts import render
from django.http import HttpResponse
from joblib import load
model = load('./savedModels/model.joblib')

# Create your views here.
def home(request):
    return render(request,'home.html')

def predictor(request):

    if request.method == 'POST':
        sepal_length= request.POST['sepal_length']
        sepal_width= request.POST['sepal_width']
        petal_length= request.POST['petal_length']
        petal_width= request.POST['petal_width']
        y_pred = model.predict([[sepal_length,sepal_width,petal_length,petal_width]])
        if y_pred[0] == 0 :
            y_pred='setosa'
        elif y_pred[0] == 1:
            y_pred='verscicolor'
        else :
            y_pred='virginica'
        return render(request,'iris.html',{'result':y_pred})
    return render(request, 'iris.html')
results = model.track(source=img, show=True, tracker="bytetrack.yaml", conf=0.5, classes=1)