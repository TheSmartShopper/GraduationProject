from datetime import datetime

from django.db import models
from django.utils.text import slugify
from phonenumber_field.modelfields import PhoneNumberField

STORE_TYPE = (
    ('HyperMarket', 'HyperMarket'),
    ('BigMarket', 'BigMarket')
)
STORE_SECTIONS = (
    ('Fruit', 'Fruit'),
    ('Veggies', 'Veggies'),
    ('Seafood', 'Seafood'),
    ('Seafood', 'Seafood'),
    ('Seafood', 'Seafood'),
    ('Meat', 'Meat'),
    ('Cereal', 'Cereal'),
    ('Coffee', 'Coffee'),
    ('Condiments', ''),
    ('Baby', 'Baby'),
    ('Pet', 'Pet'),
    ('Paper', 'Paper'),
    ('Dairy', 'Dairy'),
    ('Frozen', 'Frozen')
)


class Store(models.Model):
    Store_Slug = models.SlugField(blank=True, null=True)
    Store_Name = models.CharField(max_length=50, unique=True)
    Store_Image = models.ImageField(upload_to='StoreLogo_img', blank=True,
                                   null=True)  # will change when upload the product on S3
    Store_PhonesNumber = PhoneNumberField(null=False, blank=False, unique=True,
                                          help_text='Phone number must be entered in the format \'+999999999\'. Up to 15 digits allowed.')

    Store_Type = models.CharField(max_length=50, choices=STORE_TYPE, default='HyperMarket')
    Store_Url = models.URLField(max_length=200, blank=True, unique=True, )
    Store_Email = models.EmailField(max_length=254, blank=False, unique=True,
                                    error_messages={'required' 'Please provide your email address.',
                                                    'unique' 'An account with this email exist.'}, )

    Store_Description = models.TextField(max_length=500, )
    Store_StartHours = models.TimeField(max_length=50, )
    Store_CloseHours = models.TimeField(max_length=50, )
    Store_State = models.BooleanField()
    Store_JoinAt = models.DateField(null=True, blank=True)
    Store_Sections = models.CharField(max_length=50, choices=STORE_SECTIONS)

    def save(self, *args, **kwargs):
        if not self.StoreSlug:
            self.StoreSlug = slugify(self.Store_Name)
        super(Store, self).save(*args, **kwargs)

    def __str__(self):
        return str(self.Store_Name)

    def is_Open_now(self, *args, **kwargs):
        if datetime.time() in range(self.Store_StartHours, self.Store_CloseHours):
            self.Store_State = True
        else:
            self.Store_State = False
        return self.Store_State


# StoreLocation = location()
# QuantityintlistOfProduct = models.project()
# format location in google maps as  dd.dddddd,dd.dddddd
"""
    AdvertisementAdvertisement
    """

# ReviewList = models.ForeignKey(ReviewAttribute, on_delete=models.CASCADE,null=True,blank=True)
'''
Product_ID int
StoreID int
Product_Name String
Product_Price Double
Product_Type PRODUCT_TYPE
Product_Number_Of_Copy int
Product_Par_Code Long
Product_Description String
Product_Manufacturer String
Product_ImagePath String
revire List<Review>


'''
PRODUCT_TYPE = (
    ('anonymous', 'anonymous'),
    ('Fresh Food', 'Fresh Food'),
    ('Food Cupboard', 'Food Cupboard'),
    ('Frozen Food', 'Frozen Food'),
    ('Beverages', 'Beverages'),
    ('Bio & Organic Food', 'Bio & Organic Food'),
    ('Baby Product', 'Baby Product'),
    ('Cleaning & Household', 'Cleaning & Household'),
    ('Health & Fitness', 'Health & Fitness'),
    ('Smartphones, Tablets & Wearables', 'Smartphones, Tablets & Wearables'),
    ('Electronics & Appliances', 'Electronics & Appliances'),
    ('Home & Garden', 'Home & Garden'),
    ('Pet Supplies ', 'Pet Supplies '),
    ('Toys & OutDoor', 'Toys & OutDoor'),
    ('Stationery & School Supplies', 'Stationery & School Supplies'),
    ('Kiosk', 'Kiosk'),
    ('Automotive', 'Automotive'),
)
MANUFACTURERS = (
    ('Manufacturer 1', 'Manufacturer 1'),
    ('Manufacturer 2', 'Manufacturer 2')
)

class Product(models.Model):
    Product_Name = models.CharField(max_length=50, blank=True, null=True)
    Product_Slug = models.SlugField(blank=True, null=True)
    Product_Price = models.DecimalField(blank=True, null=True)
    Product_Type = models.CharField(max_length=50, blank=True, null=True)
    Product_Number_Of_Copy = models.IntegerField(blank=True, null=True)
    Product_Par_Code = models.IntegerField(blank=True, null=True)
    Product_Description = models.TextField(max_length=500, blank=True, null=True)
    Product_Manufacturer = models.CharField(max_length=50, choices=MANUFACTURERS ,default='anonymous Manufacturer')
    Product_ImagePath = models.CharField(max_length=50, blank=True, null=True)  # we shall edit

    def save(self, *args, **kwargs):
        if not self.Product_Slug:
            self.StoreSlug = slugify(self.Product_Slug)
        super(Product, self).save(*args, **kwargs)

    def __str__(self):
        return str(self.Product_Name)
