# from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
# from django.db import models
# class UserManager(BaseUserManager):
#     def create_user(self, email, password=None, **extra_fields):
#         if not email:
#             raise ValueError('The Email field must be set')
#         email = self.normalize_email(email)
#         user = self.model(email=email, **extra_fields)
#         user.set_password(password)
#         user.save(using=self._db)
#         return user

#     def create_superuser(self, email, password=None, **extra_fields):
#         extra_fields.setdefault('is_staff', True)
#         extra_fields.setdefault('is_superuser', True)
#         return self.create_user(email, password, **extra_fields)
 
# class User(AbstractBaseUser):
#     USER_TYPES = (
#         ('customer', 'Customer'),
#         ('delivery_person', 'Delivery Person'),
#         ('restaurant_owner', 'Restaurant Owner'),
#     )

#     user_id = models.AutoField(primary_key=True)
#     name = models.CharField(max_length=255)
#     email = models.EmailField(unique=True)
#     password = models.CharField(max_length=255)
#     phone_number = models.CharField(max_length=15)
#     address = models.TextField()
#     user_type = models.CharField(max_length=20, choices=USER_TYPES)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)
#     is_deleted = models.BooleanField(default=False)
#     is_staff = models.BooleanField(default=False)
#     is_active = models.BooleanField(default=True)
#     is_superuser = models.BooleanField(default=False)
#     objects = UserManager()
#     USERNAME_FIELD = 'email'
#     REQUIRED_FIELDS = ['name']
#     def __str__(self):
#         return self.name
#     class Meta:
#         managed = True
#         db_table = 'user'

# # Customber table 22

# from django.contrib.auth import get_user_model
# User = get_user_model()

# class CustomerDetails(models.Model):
#     from django.contrib.auth import get_user_model

#     User = get_user_model()
#     name = models.CharField(max_length=255,blank=False,null=False)
#     customer = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
#     date_of_birth = models.DateField(blank=True,null=True, max_length=20)
#     phone_number = models.CharField(max_length=15)
#     address = models.TextField()
#     profile_logo= models.FileField(null=True,blank=True,max_length=100)
    
#     def __str__(self):
#         return f"{self.customer.name}'s Details"
    
#     class Meta:
#         managed = True
#         db_table = 'customer_details'
    

# #Restaurant Model
# from django.conf import settings
# class Restaurant(models.Model):
#     restaurant_id = models.AutoField(primary_key=True)
#     name = models.CharField(max_length=500)
#     owner = models.ForeignKey(User, on_delete=models.CASCADE)
#     address = models.TextField()
#     phone_number = models.CharField(blank=False,null=False,max_length=15)
#     email = models.EmailField()
#     description = models.TextField(blank=True, null=True)
#     rating = models.DecimalField(max_digits=3, decimal_places=2, blank=True, null=True)
#     restaurant_GST = models.CharField(max_length=100, null=True, blank=True)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)
#     is_deleted= models.BooleanField(default=False)
#     def __str__(self):
#         return self.name
    
#     class Meta:
#         managed = True
#         db_table = 'restaurant_details'
        

        

# # DeliveryPerson model
# class DeliveryPerson(models.Model):
#     delivery_person_id = models.AutoField(primary_key=True)
#     user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
#     vehicle_details = models.CharField(max_length=255, blank=True, null=True)
#     availability_status = models.BooleanField(default=True)
#     rating = models.DecimalField(max_digits=3, decimal_places=2, blank=True, null=True)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)

#     def __str__(self):
#         return self.user.name

#     class Meta:
#         managed = True
#         db_table = 'delivery_persion_details'
        
        
# # MenuItem model
# class MenuItem(models.Model):
#     menu_item_id = models.AutoField(primary_key=True)
#     restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
#     name = models.CharField(max_length=255)
#     description = models.TextField(blank=True, null=True)
#     price = models.DecimalField(max_digits=10, decimal_places=2)
#     image_url = models.URLField(blank=True, null=True)
#     availability = models.BooleanField(default=True)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)
#     rating = models.DecimalField(max_digits=3, decimal_places=2, blank=True, null=True)   
#     preparation_time = models.IntegerField(help_text='Preparation time in minutes', blank=True, null=True) 

#     def __str__(self):
#         return self.name
    
#     class Meta:
#         managed = True
#         db_table = 'menuitem_details'

# # Order model
# class Order(models.Model):
#     ORDER_STATUS_CHOICES = (
#         ('pending', 'Pending'),
#         ('confirmed', 'Confirmed'),
#         ('preparing', 'Preparing'),
#         ('out_for_delivery', 'Out for Delivery'),
#         ('delivered', 'Delivered'),
#         ('cancelled', 'Cancelled'),
#     )

#     order_id = models.AutoField(primary_key=True)
#     user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
#     #restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE,default=1)
#     total_amount = models.DecimalField(max_digits=10, decimal_places=2)
#     order_status = models.CharField(max_length=20, choices=ORDER_STATUS_CHOICES, default='pending')
#     delivery_address = models.TextField()
#     order_date = models.DateTimeField(auto_now_add=True)
#     delivery_date = models.DateTimeField(blank=True, null=True)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)

#     def __str__(self):
#         return f"Order {self.order_id} for {self.customer_name}"
    
#     class Meta:
#         managed = True
#         db_table = 'order'


# # OrderItem model
# class OrderItem(models.Model):
#     order_item_id = models.AutoField(primary_key=True)
#     order = models.ForeignKey(Order, on_delete=models.CASCADE)
#     menu_item = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
#     quantity = models.PositiveIntegerField()
#     price = models.DecimalField(max_digits=10, decimal_places=2)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)

#     def __str__(self):
#         return f"{self.menu_item.name} (x{self.quantity})"
    
#     class Meta:
#         managed = True
#         db_table = 'order_item'
    
# # Payment model
# class Payment(models.Model):
#     PAYMENT_METHOD_CHOICES = (
#         ('credit_card', 'Credit Card'),
#         ('debit_card', 'Debit Card'),
#         ('net_banking', 'Net Banking'),
#         ('cash_on_delivery', 'Cash on Delivery'),
#         ('upi','UPI'),
#     )

#     payment_id = models.AutoField(primary_key=True)
#     order = models.ForeignKey(Order, on_delete=models.CASCADE)
#     payment_method = models.CharField(max_length=20, choices=PAYMENT_METHOD_CHOICES)
#     amount = models.DecimalField(max_digits=10, decimal_places=2)
#     payment_status = models.CharField(max_length=20, default='pending')
#     transaction_id = models.CharField(max_length=255, blank=True, null=True)
#     payment_date = models.DateTimeField(auto_now_add=True)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)

#     def __str__(self):
#         return f"Payment {self.payment_id} for Order {self.order.order_id}"
    
#     class Meta:
#         managed = True
#         db_table = 'payment'


# # Review model
# class Review(models.Model):
#     review_id = models.AutoField(primary_key=True)
#     user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
#     restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE, blank=True, null=True)
#     customer = models.ForeignKey(CustomerDetails, on_delete=models.CASCADE, related_name='reviews')
#     delivery_person = models.ForeignKey(DeliveryPerson, on_delete=models.CASCADE, blank=True, null=True)
#     rating = models.DecimalField(max_digits=3, decimal_places=2)
#     comment = models.TextField(blank=True, null=True)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)

#     def __str__(self):
#         return f"Review by {self.user.name}"
    
#     class Meta:
#         managed = True
#         db_table = 'review'
    
# # Category model
# class Category(models.Model):
#     category_id = models.AutoField(primary_key=True)
#     name = models.CharField(max_length=255)
#     description = models.TextField(blank=True, null=True)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)

#     def __str__(self):
#         return self.name
    
#     class Meta:
#         managed = True
#         db_table = 'category'

# # MenuItemCategory model
# class MenuItemCategory(models.Model):
#     menu_item_category_id = models.AutoField(primary_key=True)
#     menu_item = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
#     category = models.ForeignKey(Category, on_delete=models.CASCADE)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)

#     def __str__(self):
#         return f"{self.menu_item.name} - {self.category.name}"
    
#     class Meta:
#         managed = True
#         db_table = 'meanuitem_category'
    
# # Notification Model
# class Notification(models.Model):
#     notification_id = models.AutoField(primary_key=True)
#     user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
#     message = models.TextField()
#     read_status = models.BooleanField(default=False)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)

#     def __str__(self):
#         return f"Notification for {self.user.name}"
    
#     class Meta:
#         managed = True
#         db_table = 'notification'


# class RestaurantTiming(models.Model):
#     timing_id = models.AutoField(primary_key=True)
#     restaurant = models.ForeignKey('Restaurant', on_delete=models.CASCADE)
#     day_of_week = models.CharField(max_length=10)
#     opening_time = models.TimeField()
#     closing_time = models.TimeField()
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)

#     def __str__(self):
#         return f"{self.restaurant.name} - {self.day_of_week}"
    
#     class Meta:
#         managed = True
#         db_table = 'restaurant_timing'
    
# from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
# from django.db import models

# class UserManager(BaseUserManager):
#     def create_user(self, email, password=None, **extra_fields):
#         if not email:
#             raise ValueError('The Email field must be set')
#         email = self.normalize_email(email)
#         user = self.model(email=email, **extra_fields)
#         user.set_password(password)
#         user.save(using=self._db)
#         return user

#     def create_superuser(self, email, password=None, **extra_fields):
#         extra_fields.setdefault('is_staff', True)
#         extra_fields.setdefault('is_superuser', True)
#         return self.create_user(email, password, **extra_fields)


from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db import models
from django.conf import settings

class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(email, password, **extra_fields)

class User(AbstractBaseUser):
    USER_TYPES = (
        ('customer', 'Customer'),
        ('delivery_person', 'Delivery Person'),
        ('restaurant_owner', 'Restaurant Owner'),
    )
    user_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=15)
    address = models.TextField()
    user_type = models.CharField(max_length=20, choices=USER_TYPES)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_deleted = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def __str__(self):
        return self.name

    class Meta:
        managed = True
        db_table = 'user'

class CustomerDetails(models.Model):
    customer = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, primary_key=True)
    name = models.CharField(max_length=255)
    date_of_birth = models.DateField(blank=True, null=True)
    phone_number = models.CharField(max_length=15)
    address = models.TextField()
    profile_logo = models.FileField(null=True, blank=True, max_length=100)

    def __str__(self):
        return f"{self.customer.name}'s Details"

    class Meta:
        managed = True
        db_table = 'customer_details'

class Restaurant(models.Model):
    restaurant_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=500)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    address = models.TextField()
    phone_number = models.CharField(max_length=15)
    email = models.EmailField()
    description = models.TextField(blank=True, null=True)
    rating = models.DecimalField(max_digits=3, decimal_places=2, blank=True, null=True)
    restaurant_GST = models.CharField(max_length=100, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_deleted = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    class Meta:
        managed = True
        db_table = 'restaurant_details'

class DeliveryPerson(models.Model):
    delivery_person_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    vehicle_details = models.CharField(max_length=255, blank=True, null=True)
    availability_status = models.BooleanField(default=True)
    rating = models.DecimalField(max_digits=3, decimal_places=2, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.name

    class Meta:
        managed = True
        db_table = 'delivery_person_details'

class MenuItem(models.Model):
    menu_item_id = models.AutoField(primary_key=True)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image_url = models.URLField(blank=True, null=True)
    availability = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    rating = models.DecimalField(max_digits=3, decimal_places=2, blank=True, null=True)
    preparation_time = models.IntegerField(help_text='Preparation time in minutes', blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        managed = True
        db_table = 'menu_item_details'

class Order(models.Model):
    ORDER_STATUS_CHOICES = (
        ('pending', 'Pending'),
        ('confirmed', 'Confirmed'),
        ('preparing', 'Preparing'),
        ('out_for_delivery', 'Out for Delivery'),
        ('delivered', 'Delivered'),
        ('cancelled', 'Cancelled'),
    )

    order_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default=1)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    order_status = models.CharField(max_length=20, choices=ORDER_STATUS_CHOICES, default='pending')
    delivery_address = models.TextField()
    order_date = models.DateTimeField(auto_now_add=True)
    delivery_date = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Order {self.order_id} for {self.user.name}"

    class Meta:
        managed = True
        db_table = 'order'

class OrderItem(models.Model):
    order_item_id = models.AutoField(primary_key=True)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    menu_item = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.menu_item.name} (x{self.quantity})"

    class Meta:
        managed = True
        db_table = 'order_item'

class Payment(models.Model):
    PAYMENT_METHOD_CHOICES = (
        ('credit_card', 'Credit Card'),
        ('debit_card', 'Debit Card'),
        ('net_banking', 'Net Banking'),
        ('cash_on_delivery', 'Cash on Delivery'),
        ('upi', 'UPI'),
    )

    payment_id = models.AutoField(primary_key=True)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    payment_method = models.CharField(max_length=20, choices=PAYMENT_METHOD_CHOICES)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_status = models.CharField(max_length=20, default='pending')
    transaction_id = models.CharField(max_length=255, blank=True, null=True)
    payment_date = models.DateTimeField(auto_now_add=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Payment {self.payment_id} for Order {self.order.order_id}"

    class Meta:
        managed = True
        db_table = 'payment'

class Review(models.Model):
    review_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE, blank=True, null=True)
    customer = models.ForeignKey(CustomerDetails, on_delete=models.CASCADE, related_name='reviews')
    delivery_person = models.ForeignKey(DeliveryPerson, on_delete=models.CASCADE, blank=True, null=True)
    rating = models.DecimalField(max_digits=3, decimal_places=2)
    comment = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Review by {self.user.name}"

    class Meta:
        managed = True
        db_table = 'review'

class Category(models.Model):
    category_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        managed = True
        db_table = 'category'

class MenuItemCategory(models.Model):
    menu_item_category_id = models.AutoField(primary_key=True)
    menu_item = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.menu_item.name} - {self.category.name}"

    class Meta:
        managed = True
        db_table = 'menu_item_category'

class Notification(models.Model):
    notification_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)

    def __str__(self):
        return f"Notification for {self.user.name}"

    class Meta:
        managed = True
        db_table = 'notification'

class Coupon(models.Model):
    coupon_id = models.AutoField(primary_key=True)
    code = models.CharField(max_length=50, unique=True)
    description = models.TextField(blank=True, null=True)
    discount_percentage = models.DecimalField(max_digits=5, decimal_places=2)
    max_discount_amount = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    valid_from = models.DateTimeField()
    valid_to = models.DateTimeField()
    active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.code

    class Meta:
        managed = True
        db_table = 'coupon'


