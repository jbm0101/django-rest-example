from djongo import models
from django.core.validators import RegexValidator

class Item(models.Model):
    
    # item_name is made primary to avoide creating a brand new id 
    # field as it does not make sense in this usecase besides that 
    # Meta.managed = False because this version of django is not 
    # letting me create abstract class for item.
    
    # abstarct class is a phenomenon which are generally not used 
    # for creating their own collections rather they are used to 
    # get included in some other higher level model or class.
    item_name = models.CharField(max_length = 140, primary_key = True)    
    item_quantity = models.FloatField()
    item_price = models.FloatField()
    
    class Meta: # works like an options dictionary for model
        
        # declaring managed = True will make django think 
        # that there is no need to create collection for 
        # this without making it abstract.
        managed = False
        
        # abstract = True
        
        
        # abstarct class is a phenomenon which are generally not used 
        # for creating their own collections rather they are used to 
        # get included in some other higher level model or class.

class Order(models.Model):
    email = models.EmailField(name = "email") 
    name = models.CharField(max_length = 30, help_text="Enter Customer Name", name = "name")
    
    # modified CharField to validate mobile numbers upto 15 digits.
    phoneNumberRegex = RegexValidator(regex = r"^\+?1?\d{8,15}$")
    mobile = models.CharField(primary_key = True, validators = [phoneNumberRegex], max_length = 15, blank = False)
    
    address = models.CharField(max_length = 250, help_text="Enter customer's Address", name = "address")
     
    # to create array containing objects of other 
    # model which in this case is Item Model
    items = models.ArrayField(model_container = Item, null = True) 

    objects = models.DjongoManager()