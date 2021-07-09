from django.db import models


# Owner has a one-to-many relationship with Pet
class Owner(models.Model):
    first_name = models.CharField(max_length=30)  # first_name varchar(30)
    last_name = models.CharField(max_length=30)
    phone = models.CharField(max_length=30, default='123-456-7890')

    def __str__(self):
        return f"{self.first_name} {self.last_name}, {self.phone}"


# Pet has a many-to-one relationship with Owner
class Pet(models.Model):
    owner = models.ForeignKey(Owner, on_delete=models.CASCADE)
    breed = models.CharField(max_length=200)
    name = models.CharField(max_length=30)
    age = models.IntegerField(default=0)
    DOG = "DO"
    CAT = "CA"
    BIRD = "BI"
    REPTILE = "RE"
    OTHER = "OT"
    ANIMAL_TYPE_CHOICES = [
        (DOG, "Dog"),
        (CAT, "Cat"),
        (BIRD, "Bird"),
        (REPTILE, "Reptile"),
        (OTHER, "Other")
    ]
    animal_type = models.CharField(max_length=2, choices=ANIMAL_TYPE_CHOICES, default=OTHER)

    def is_senior(self):
        return self.age >= 10

    def __str__(self):
        return f"{self.breed}, {self.name}, {self.age}"

    class Meta:
        ordering = ["-name"]




