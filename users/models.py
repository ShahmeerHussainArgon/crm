from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()


# class Profile(models.Model):
#     ROLE_CHOICES = [
#         ('Employee', 'Employee'),
#         ('HR', 'HR'),
#         ('Admin', 'Admin'),
#         ('Leads', 'Leads'),
#         ('Project Manager', 'Project Manager'),
#     ]
#
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='Employee')
#
#     def __str__(self):
#         return f"{self.user.username} - {self.role}"


# from django.db import models
# from django.contrib.auth.models import User
#
class Skill(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Profile(models.Model):
    ROLE_CHOICES = [
        ('Employee', 'Employee'),
        ('HR', 'HR'),
        ('Admin', 'Admin'),
        ('Leads', 'Leads'),
        ('Project Manager', 'Project Manager'),
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='Employee')
    cnic = models.CharField(max_length=13, unique=True,blank=True, null=True)  # CNIC with 13 digits
    date_of_joining = models.DateField(blank=True, null=True)
    designation = models.CharField(max_length=100,blank=True, null=True)
    salary = models.DecimalField(max_digits=10, decimal_places=2,blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    mobile_number = models.CharField(max_length=15,blank=True, null=True)
    address = models.TextField()
    emergency_phone_number = models.CharField(max_length=15,blank=True, null=True)
    skills = models.ManyToManyField(Skill, related_name='profiles', blank=True)  # Skills in Profile

    def __str__(self):
        return f"{self.user.username} - {self.role}"

