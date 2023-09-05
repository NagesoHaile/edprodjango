from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
import datetime

class AccounManager(BaseUserManager):
    def create_user(self,email,username,first_name,last_name,age,password=None):
        if not email:
            raise ValueError("User must have email address")
        if not username:
            raise ValueError("User must have username")
        
        user = self.model(
            email = self.normalize_email(email),
            username = username,
            first_name = first_name,
            last_name = last_name,
            age =age
        )
        user.set_password(password)
        user.save(using=self._db)
        return user 
    def create_superuser(self,username,email,first_name,last_name,age,password):
        user = self.create_user(
            email=self.normalize_email(email),
            password=password,
            username=username,
            first_name=first_name,
            last_name=last_name,
            age=age)
        user.is_admin =True
        user.is_staff = True
        user.is_superuser =True
        user.save(using=self._db)
        return user

class User(AbstractBaseUser):
    email = models.EmailField(verbose_name="email",max_length=60, unique=True)
    username = models.CharField(max_length=30,unique=True)
    date_joined = models.DateTimeField(verbose_name="date joined",auto_now_add=True)
    last_login = models.DateTimeField(verbose_name="last login",auto_now=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    first_name = models.CharField(max_length=60)
    middle_name = models.CharField(max_length=60)
    last_name = models.CharField(max_length=60)
    age = models.DateField(default=datetime.date.today) 
    phone_number = models.CharField(max_length=15)
    birth_place = models.CharField(max_length=50)
    current_address = models.CharField(max_length=50)
    occupation = models.CharField(max_length=50,blank=True,null=True)
    profile_pic = models.ImageField(upload_to='image',blank=True,null=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username','first_name','middle_name','last_name','phone_number','birth_place','current_address','age']           

    



# Member Model
class Member(models.Model):
    # member_id = models.AutoField(primary_key=True)
    # username = models.CharField(max_length=50, unique=True)
    # password = models.CharField(max_length=100)
    first_name = models.CharField(max_length=50)
    middle_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    # phone = models.CharField(max_length=15)

    def __str__(self):
       return self.first_name +" "+ self.middle_name
    
# Admin Model
class Admin(models.Model):
    admin_id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=100)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    # phone = models.CharField(max_length=15)

    # Other admin-specific fields here

    def __str__(self):
        return self.username
    

# Event Model
class Event(models.Model):
    event_id = models.AutoField(primary_key=True)
    event_name = models.CharField(max_length=100)
    event_date = models.DateField()
    event_location = models.CharField(max_length=100)

    # Other event-specific fields here

    def __str__(self):
        return self.event_name
    
# Contribution Model
class Contribution(models.Model):
    contribution_id = models.AutoField(primary_key=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_date = models.DateField()
    member = models.ForeignKey(Member, on_delete=models.CASCADE)

    # Other contribution-specific fields here

    def __str__(self):
        return f"Contribution #{self.contribution_id}"

# Benefit Model
class Benefit(models.Model):
    benefit_id = models.AutoField(primary_key=True)
    benefit_type = models.CharField(max_length=100)
    eligibility_criteria = models.TextField()
    member = models.ForeignKey(Member, on_delete=models.CASCADE)

    # Other benefit-specific fields here

    def __str__(self):
        return self.benefit_type

# Profile Model
class Profile(models.Model):
    profile_id = models.AutoField(primary_key=True)
    address = models.TextField()
    birth_date = models.DateField()
    profile_picture = models.ImageField(upload_to='profile_pics/', blank=True, null=True)
    member = models.OneToOneField(Member, on_delete=models.CASCADE)

    # Other profile-specific fields here

    def __str__(self):
        return f"Profile of {self.member.username}"

# MemberFamily Model
class MemberFamily(models.Model):
    family_id = models.AutoField(primary_key=True)
    relationship = models.CharField(max_length=50)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    member = models.ForeignKey(Member, on_delete=models.CASCADE)

    # Other family member-specific fields here

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

