from django.shortcuts import render
from django.http import request
from .models import Message,Product
from .serializer import ProductSerializer

cart=[]
# Create your views here.
def getHome(request):
    return render(request, 'base.html')

def getContact(request):
    if request.method == 'POST':
        message = Message(
            name=request.POST['name'], 
            email=request.POST['email'],
            message=request.POST['message'])
        message.save()
    return render(request, 'contact.html')

def getProducts(request,data=1):
    products=Product.objects.all()
    serializer=ProductSerializer(products, many=True)
    if request.method == "POST":
        cart.append(eval(data))
        return render(request,'products.html',{'data':serializer.data, "cart":[]})
    return render(request,'products.html',{'data':serializer.data, "cart":[]})

def getCart(request):
    total = 0
    if request.method == 'POST':
        return render(request, "cart.html",{"data":[],'total':total})
    for i in cart:
        total += eval(i['price'])
    return render(request, "cart.html",{"data":cart, 'total':total})
