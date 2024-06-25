"""
URL configuration for khanaprj project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
#from . import views  
from khanaapp.views import UserRegistrationView, LoginView,RestaurantView,CustomerDetailsCreateView,CustomerDetailsRetrieveUpdateView
from khanaapp.views import DeliveryPersonCreateView, DeliveryPersonRetrieveUpdateView,MenuItemListCreate, MenuItemRetrieveUpdateDestroy,getalluser


urlpatterns = [
    path('admin/', admin.site.urls),
    # path('', include('khanaapp.urls')),
    path('register/', UserRegistrationView.as_view(), name='user-registration'),
    path('register/<int:user_id>/', UserRegistrationView.as_view(), name='fetch_user_details'),
    path('user/', getalluser.as_view(), name='fetch_All_user_details'),############
    path('login/', LoginView.as_view(), name='user-login'),
    path('customer-details/', CustomerDetailsCreateView.as_view(), name='customer-details-create'),
    path('customer-details/<int:customer_id>/', CustomerDetailsRetrieveUpdateView.as_view(), name='customer-details-retrieve-update'),
    path('restaurant/', RestaurantView.as_view(), name='create_restaurant'),
    path('restaurant/<int:restaurant_id>/', RestaurantView.as_view(), name='get_update_delete_restaurant'),
    path('delivery-person/', DeliveryPersonCreateView.as_view(), name='delivery-person-create'),
    path('delivery-person/<int:delivery_person_id>/', DeliveryPersonRetrieveUpdateView.as_view(), name='delivery-person-retrieve-update'),
    path('menu-items/', MenuItemListCreate.as_view(), name='menu-item-list-create'),
    path('menu-items/<int:pk>/', MenuItemRetrieveUpdateDestroy.as_view(), name='menu-item-detail'),
]