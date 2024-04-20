from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework import viewsets, status
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
    
from django.contrib.auth.models import User
from rest_framework.response import Response
from .models import *
from .serializers import *
from .utils import sentiment

# Testing Route
@api_view(["GET"])
def home(request):
    message = "Hello World! I am Live!"
    return Response(message)

@api_view(["GET"])
def get_product(request, product_id):
    product = Product.objects.get(id=product_id)
    serializer = ProductSerializer(product)
    return Response(serializer.data)


class RegisterAPI(APIView):
    def post(self, request):
        data = request.data
        serializer = RegisterSerializer(data=data)

        if not serializer.is_valid():
            return Response({
                "status": False,
                "message": serializer.errors
            }, status.HTTP_400_BAD_REQUEST)

        serializer.save()
        
        return Response({
            "status": "True",
            "message": "User Created",
        }, status.HTTP_201_CREATED)
    
class LoginAPI(APIView):
    def post(self ,request):
        data = request.data
        serializer = LoginSerializer(data = data)

        if not serializer.is_valid():
            return Response({
                "status": False,
                "message": serializer.errors
            }, status.HTTP_400_BAD_REQUEST)
        
        user = authenticate(username = serializer.data["username"], password = serializer.data["password"])
        if not user:
            return Response({
                "status": False,
                "message": "Invalid Credentials"
            }, status.HTTP_400_BAD_REQUEST)

        token, _ = Token.objects.get_or_create(user=user)

        return Response({
            "status": "True",
            "message": "User Logged In",
            "token": str(token)
        }, status.HTTP_201_CREATED)

@api_view(["GET"])
def get_customers(request):
    # Query all users excluding superusers
    customers = User.objects.filter(is_superuser=False)
    serializer = UserSerializer(customers, many=True)

    return Response(serializer.data)

class ProductAPI(APIView):
    def get(self, request):
        objs = Product.objects.all()
        serializer = ProductSerializer(objs, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        data = request.data
        serializer = ProductSerializer(data = data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        
        return Response(serializer.errors)

    def patch(self, request):
        data = request.data
        obj = Product.objects.get(id = data["id"])
        serializer = ProductSerializer(obj, data = data, partial = True)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        
        return Response(serializer.errors)
    
    def delete(self, request):
        data = request.data
        obj = Product.objects.get(id = data["id"])
        obj.delete()

        return Response({"message": "Data Deleted", "data": data})

class CustomerViewSet(viewsets.ModelViewSet):
    serializer_class = CustomerSerializer
    queryset = Customer.objects.all()

class SentimentAPI(APIView):
    def get(self, request):
        objs = Sentiment.objects.all()
        serializer = SentimentSerializer(objs, many=True)
        return Response(serializer.data)
    
    def post(self, request):    
        data = request.data
        # Evaluating Sentiment of the Comment
        data["sentiment"] = sentiment.roberta_predict(data["comment"])
        serializer = SentimentSerializer(data = data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        
        return Response(serializer.errors)

    def patch(self, request):
        data = request.data
        obj = Sentiment.objects.get(id = data["id"])
        serializer = SentimentSerializer(obj, data = data, partial = True)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        
        return Response(serializer.errors)
    
    def delete(self, request):
        data = request.data
        obj = Sentiment.objects.get(id = data["id"])
        obj.delete()

        return Response({"message": "Data Deleted", "data": data})

class SaleViewSet(viewsets.ModelViewSet):
    serializer_class = SaleSerializer
    queryset = Sale.objects.all()
