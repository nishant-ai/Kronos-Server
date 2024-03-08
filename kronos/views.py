from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Product
from .serializers import ProductSerializer

@api_view(["GET"])
def home(request):
    message = "Hello World! I am Live!"
    return Response(message)

@api_view(["GET", "POST", "PATCH", "DELETE"])
def product(request):

    if request.method == "GET":
        objs = Product.objects.all()
        serializer = ProductSerializer(objs, many=True)
        return Response(serializer.data)
    
    elif request.method == "POST":
        data = request.data
        serializer = ProductSerializer(data = data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        
        return Response(serializer.errors)
