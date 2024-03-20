from django.db import models

# Create your models here.
class Owner(models.Model):
    name = models.CharField(max_length=50, null=False, blank=False)
    age = models.PositiveIntegerField(null=False, blank=False)
    number_of_pets = models.PositiveIntegerField(null=False, blank=False, default = 0)
    
    def __str__(self):
        return f'{self.name} is {self.age} and has {self.number_of_pets} pets.'
    
    def update_number_of_pets(self, new_number_of_pets):
        self.number_of_pets = new_number_of_pets
        self.save()
    
class Cat(models.Model):
    breed = models.CharField(max_length=50, null=False, blank=False)
    age = models.PositiveIntegerField(null=False, blank=False, default = 0)
    vaccinated = models.BooleanField(default=False)
    description = models.TextField(null=False, blank=False)
    name = models.CharField(max_length=50, null=False, blank=False)
    
    def __str__(self):
        return f"{self.name} is a {self.breed} that is {self.age} years old and {'is vaccinated' if self.vaccinated else 'is not vaccinated'}"
    
    def update_vaccination_status(self):
        self.vaccinated = not self.vaccinated
        self.save()
        
    def set_new_age(self, new_age):
        self.age = new_age
        self.save()
    
class Dog(models.Model):
    breed = models.CharField(max_length=50, null=False, blank=False)
    age = models.PositiveIntegerField(null=False, blank=False, default = 0)
    vaccinated = models.BooleanField(default=False)
    description = models.TextField(null=False, blank=False)
    name = models.CharField(max_length=50, null=False, blank=False)
    
    def __str__(self):
        return f"{self.name} is a {self.breed} that is {self.age} years old and {'is vaccinated' if self.vaccinated else 'is not vaccinated'}"
    
    def update_vaccination_status(self):
        self.vaccinated = not self.vaccinated
        self.save()
        
    def set_new_age(self, new_age):
        self.age = new_age
        self.save()
    
class ExoticAnimal(models.Model):
    region_of_origin = models.CharField(max_length=50, null=False, blank=False)
    age = models.PositiveIntegerField(null=False, blank=False, default = 0)
    type_of_animal = models.CharField(max_length=50, null=False, blank=False)
    description = models.TextField(null=False, blank=False)
    name = models.CharField(max_length=50, null=False, blank=False)
    
    def __str__(self):
        return f'{self.name} is a {self.type_of_animal} that is from {self.region_of_origin} and is {self.age} years old'