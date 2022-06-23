from djongo import models

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
    email = models.EmailField(primary_key = True, name = "email") 
    name = models.CharField(max_length = 30, help_text="Enter Customer Name", name = "name")
    address = models.CharField(max_length = 250, help_text="Enter customer's Address", name = "address")
     
    # to create array containing objects of other 
    # model which in this case is Item Model
    items = models.ArrayField(model_container = Item, null = True) 

    objects = models.DjongoManager()