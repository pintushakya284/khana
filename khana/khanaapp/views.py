from django.shortcuts import render
from rest_framework.authtoken.models import Token
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import User
from .serializers import UserSerializer, LoginSerializer
from django.http import JsonResponse


##____________________________________________________This Section Is User Profile_____________________________________________________#####
class UserRegistrationView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "User created successfully"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
    def get(self, request, user_id=None):
        if user_id is None:
            return Response(
                {"error": "user_id not provided"},
                status=status.HTTP_400_BAD_REQUEST
            )

        try:
            user = get_object_or_404(User, pk=user_id, is_deleted=False)
            serializer = UserSerializer(user)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            logger.error(f"Error fetching user with user_id {user_id}: {str(e)}")
            return Response(
                {"error": "User not found "},
                status=status.HTTP_404_NOT_FOUND
            )
            
class getalluser(APIView):     
    #permission_classes = [IsAuthenticated]  # Uncomment to require authentication
    def get(self, request):
        users = User.objects.filter(is_deleted=False)  # Filter for active users only
        serializer = UserSerializer(users, many=True)  # Serialize all users
        return Response(serializer.data, status=200)
    
#______________________________user login pagee ________________________________
class LoginView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = LoginSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            user = serializer.validated_data['user']
            token, created = Token.objects.get_or_create(user=user)
            return Response({"token": token.key, "user_id": user.user_id}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# from django.contrib.auth import authenticate
# class LoginView(APIView):
#     def post(self, request, *args, **kwargs):
#         username = request.data.get('username')
#         password = request.data.get('password')
        
#         user = authenticate(username=username, password=password)
#         if user:
#             # Authentication successful
#             token, created = Token.objects.get_or_create(user=user)
#             return Response({"token": token.key, "user_id": user.user_id}, status=status.HTTP_200_OK)
#         else:
#             # Authentication failed
#             return Response({"error": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED)

# from django.contrib.auth import authenticate, login
# from django.shortcuts import render, redirect
# from django.contrib.auth.decorators import login_required  # Optional: for protected views

# def user_login(request):
#     if request.method == 'POST':
#         email = request.POST['email']
#         password = request.POST['password']
#         # Authenticate user using email
#         user = authenticate(request, username=email, password=password)
#         if user is not None:
#             login(request, user)
#             # Redirect to desired page after successful login (e.g., home page)
#             return redirect('home')
#         else:
#             # Login failed - display error message in the template
#             login_error = 'Invalid email or password.'
#             return render(request, 'login.html', {'login_error': login_error})
#     # GET request: Render the login form
#     return render(request, 'login.html')
# # Optional: Decorate views requiring authentication
# @login_required
# def protected_view(request):
#     """
#     Example view that can only be accessed by logged-in users.
#     """
#     # ... Protected view logic ...
#     return render(request, 'protected_view.html')

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import User, CustomerDetails
from .serializers import UserSerializer, CustomerDetailsSerializer
from django.db import transaction
from .serializers import UserSerializer, CustomerDetailsSerializer

# views.py
from django.contrib.auth import get_user_model
from .serializers import UserSerializer, CustomerDetailsSerializer
from .models import CustomerDetails

from rest_framework import generics
from .models import CustomerDetails
from .serializers import CustomerDetailsSerializer


class CustomerDetailsCreateView(generics.CreateAPIView):
    queryset = CustomerDetails.objects.all()
    serializer_class = CustomerDetailsSerializer

class CustomerDetailsRetrieveUpdateView(generics.RetrieveUpdateAPIView):
    queryset = CustomerDetails.objects.all()
    serializer_class = CustomerDetailsSerializer
    lookup_field = 'customer_id'

    
class CustomerDetailsView(APIView):
    def get(self, request, user_id):
        try:
            customer_details = CustomerDetails.objects.get(customer=user_id)
            serializer = CustomerDetailsSerializer(customer_details)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except CustomerDetails.DoesNotExist:
            return Response({"message": "Customer details not found"}, status=status.HTTP_404_NOT_FOUND)
    
    def put(self, request, user_id):
        try:
            customer_details = CustomerDetails.objects.get(customer=user_id)
            serializer = CustomerDetailsSerializer(customer_details, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except CustomerDetails.DoesNotExist:
            return Response({"message": "Customer details not found"}, status=status.HTTP_404_NOT_FOUND)
        
        
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from .models import Restaurant
from .serializers import RestaurantSerializer
import logging

logger = logging.getLogger(__name__)

class RestaurantView(APIView):
    def post(self, request, *args, **kwargs):
        try:
            logger.debug(f"Request data: {request.data}")
            serializer = RestaurantSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                logger.info('Restaurant Details created successfully')
                return Response({"message": "Restaurant Details created successfully"}, status=status.HTTP_201_CREATED)
            logger.error('Error in creating restaurant: %s', serializer.errors)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            logger.exception('Unexpected error in creating restaurant')
            return Response({"message": "An unexpected error occurred"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
    def put(self, request, restaurant_id, *args, **kwargs):
        restaurant = get_object_or_404(Restaurant, restaurant_id=restaurant_id)
        serializer = RestaurantSerializer(restaurant, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            logger.info('Restaurant updated Details successfully')
            return Response({"message": "Restaurant updated Details successfully"}, status=status.HTTP_200_OK)
        logger.error('Error in updating restaurant: %s', serializer.errors)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def get(self, request, restaurant_id, *args, **kwargs):
        restaurant = get_object_or_404(Restaurant, restaurant_id=restaurant_id)
        serializer = RestaurantSerializer(restaurant)
        logger.info('Restaurant details retrieved successfully')
        return Response(serializer.data, status=status.HTTP_200_OK)

    def delete(self, request, restaurant_id, *args, **kwargs):
        restaurant = get_object_or_404(Restaurant, restaurant_id=restaurant_id)
        restaurant.delete()
        logger.info('Restaurant deleted successfully')
        return Response({"message": "Restaurant deleted successfully"}, status=status.HTTP_204_NO_CONTENT)



# delivery_person/views.py

from rest_framework import generics
from .models import DeliveryPerson
from .serializers import DeliveryPersonSerializer

class DeliveryPersonCreateView(generics.CreateAPIView):
    queryset = DeliveryPerson.objects.all()
    serializer_class = DeliveryPersonSerializer

class DeliveryPersonRetrieveUpdateView(generics.RetrieveUpdateAPIView):
    queryset = DeliveryPerson.objects.all()
    serializer_class = DeliveryPersonSerializer
    lookup_field = 'delivery_person_id'


# views.py
from rest_framework import generics
from .models import MenuItem
from .serializers import MenuItemSerializer

class MenuItemListCreate(generics.ListCreateAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer

class MenuItemRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer
