from django.db import models


<<<<<<< HEAD
class Categorie(models.Model):
=======
class Designs3D(models.Model):
    category_name = models.CharField(max_length=255)
    category_image = models.ImageField(upload_to='category')
>>>>>>> b49266201a57404140876bdf782266f06847d32c
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.category_name

class Blog(models.Model):
    title = models.CharField(max_length=600)
    category = models.ForeignKey(Designs3D, on_delete=models.CASCADE)
    content = models.TextField()
    image_one = models.ImageField(upload_to='blog/', null=True, blank=True)
    image_two = models.ImageField(upload_to='blog/', null=True, blank=True)
    image_three = models.ImageField(upload_to='blog/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Contact(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField()
    contact = models.CharField(max_length=15)
    notes = models.TextField()
    posted_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.first_name + '  ' + self.last_name + '  |  ' + self.email

class Image(models.Model):
    category = models.ForeignKey(Designs3D, on_delete=models.CASCADE)
    Image = models.ImageField(upload_to='display')


class Vastu(models.Model):
    title = models.CharField(max_length=255)
    Image = models.ImageField(upload_to='display')