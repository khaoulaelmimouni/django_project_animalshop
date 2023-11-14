from django.conf import settings
from django.db import models
from django.utils import timezone

"""class Equipement(models.Model):
    id_equip = models.CharField(max_length=100, primary_key=True)
    disponibilite = models.CharField(max_length=20)
    photo = models.CharField(max_length=200)
    def __str__(self):
        return self.id_equip"""

"""class Character(models.Model):
    id_character = models.CharField(max_length=100, primary_key=True)
    etat = models.CharField(max_length=20)
    type = models.CharField(max_length=20)
    race = models.CharField(max_length=20)
    photo = models.CharField(max_length=200)
    lieu = models.ForeignKey(Equipement, on_delete=models.CASCADE)
    def __str__(self):
        return self.id_character"""

class farmer(models.Model):
    """
    this is the famer table with attributes name,email,password,dob,address
    """
    f_id=models.CharField(max_length=50,primary_key=True)
    name=models.CharField(max_length=50,default='')
    email=models.CharField(max_length=50,default='')
    password=models.CharField(max_length=200)
    street=models.CharField(max_length=30,default='')
    city=models.CharField(max_length=30,default='')
    district=models.CharField(max_length=30,default='')
    phone=models.CharField(default=0,max_length=12)
    selling= models.IntegerField(default=0,blank=True,null=True)

    def increment_selling(self):
        return self.selling+1
    
    def __str__(self):
        return self.name
    

class sell_animal(models.Model):

    animal_id=models.AutoField(primary_key=True)
    animal_name=models.CharField(max_length=50)
    description=models.CharField(max_length=100)
    f_id=models.ForeignKey(farmer,on_delete=models.CASCADE,related_name='famer')
    quantity=models.CharField(max_length=20)
    animal_race=models.CharField(max_length=20,default='')
    price=models.IntegerField()
    photo = models.CharField(max_length=20)
    def __str__(self):
        return self.animal_name

class buy(models.Model):
   
    p_id=models.ForeignKey(sell_animal,on_delete=models.CASCADE,related_name='sell')
    f_id=models.ForeignKey(farmer,on_delete=models.CASCADE,related_name='farmer')
    date=models.DateField()
    def __str__(self):
        return self.date
