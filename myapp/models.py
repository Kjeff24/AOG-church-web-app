from django.db import models


class Profile(models.Model):
    name = models.CharField(max_length=100)
    city = models.CharField(max_length=200,default="Accra")
    position = models.CharField(max_length=100)
    rating = models.DecimalField(max_digits=3, decimal_places=1)
    phone_number = models.CharField(max_length=20)
    address = models.CharField(max_length=200)
    email = models.EmailField()
    birthday = models.DateField()
    gender = models.CharField(max_length=10, choices=[('male', 'Male'), ('female', 'Female')])
    image = models.ImageField(upload_to='profileImages/', null=True, default="avatar.svg")

    def __str__(self):
        return self.name


class CurrentNews(models.Model):
    image = models.ImageField(upload_to='NewImages/', null=True, default="avatar.svg")
    headline = models.CharField(max_length=200)
    headlineLink = models.CharField(max_length=200)
    content = models.TextField()
    pub_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.headline

class LiveSession(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    datetime = models.DateField()
    speaker = models.CharField(max_length=200)
    youtubeLink = models.TextField(blank=True)
    pub_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

