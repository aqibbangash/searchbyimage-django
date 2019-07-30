from django.shortcuts import render
from django.http import HttpResponse
import json
from .forms import InventoryForm
from .predict import predict
from .models import Inventory
from django.conf import settings
from django.core import serializers
from .models import Cocktails
from .convertIngredients import convertIngredients
from itertools import chain
import requests

# Create your views here.


def getcocktails(data):
    # inventory = Inventory.objects.all()
    # cList = []
    #
    # cs = Cocktails.objects.all()
    # for i in inventory:
    #     # print i.prediction
    #     if not cs.filter(ingredients__icontains=i.prediction):
    #         continue
    #     else:
    #         cList.append(cs.filter(ingredients__icontains=i.prediction))
    #
    # cs = list(chain(cs))
    # for c in cs:
    #     print(c.name)
    # data = serializers.serialize("json", data)
    print("Respons to show")

    # r = requests.post('http://127.0.0.1:8000/recommendations', data)
    #
    # print(r)
    data = json.dumps(data)

    # return HttpResponse(json.loads(data), content_type='application/json')


def postimage(request):

    data = None

    if request.method == 'POST':
        form = InventoryForm(request.POST, request.FILES)
        print(form.is_valid())
        if form.is_valid():
            try:
                print('i am in try')
                data = predict.run(request.FILES['image'])
                print("i have recived something.. here it is:\n  ", data)
            except:
                print('Some thing going wrong for input')
                pass
            instance = Inventory(image=request.FILES['image'], prediction=data)
            instance.save()
            # image = instance.image

        # getcocktails(data)
        # data = {'data': 'otherdata'}
        # data = request.FILES
        # Inventory.objects.create(image=data)
        # Inventory.save()
        # return HttpResponse(json.dumps(response), content_type='application/json; charset=utf-8')

        # data = predict.run(data)
        print("Respons to show")


        # r = requests.post('http://127.0.0.1:8000/recommendations', data)

        # print(r)
        # return render(r, 'recommendations.html')

        return HttpResponse(json.dumps(data), content_type='application/json; charset=utf-8')

    else:
        return HttpResponse(
            json.dumps({"nothing to see": "this isn't happening"}),
            content_type="application/json"
        )


def make_cond(name, value):
    cond = json.dumps({name: value})[1:-1]  # remove '{' and '}'
    return ' ' + cond  # avoid '\"'
