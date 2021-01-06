from django.db import models


class Designs3D(models.Model):
    category_name = models.CharField(max_length=255)
    category_image = models.ImageField(upload_to='category')
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

class All_Images(models.Model):
    category = models.ForeignKey(Designs3D, on_delete=models.CASCADE)
    Image = models.ImageField(upload_to='display')


class Interior_Designing(models.Model):
    title = models.CharField(max_length=255)
    Image = models.ImageField(upload_to='display')


class Flat_decor(models.Model):
    title = models.CharField(max_length=255)
    Image = models.ImageField(upload_to='display')

class Vastu(models.Model):
    title = models.CharField(max_length=255)
    Image = models.ImageField(upload_to='display')