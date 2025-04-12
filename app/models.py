from django.db import models

# Create your models here.
"""Model for About me on Portfolio"""
class AboutMe(models.Model):
    description = models.TextField()

    class Meta:
        verbose_name = 'About me'
        verbose_name_plural = 'About me'

    def __str__(self):
        return 'Description about me'


"""Model for Skills on Portfolio"""
class Skill(models.Model):
    name = models.CharField(max_length=100)
    rating = models.IntegerField()

    def __str__(self):
        return self.name


"""Model for Tecgnologies & Tools on portfolio"""
class TechTools(models.Model):
    name = models.CharField(max_length=100)
    img = models.ImageField(upload_to='img')

    class Meta:
        verbose_name = 'Tech tool'
        verbose_name_plural = 'Tech tools'

    def __str__(self):
        return self.name


"""Model for Recent Projects on portfolio"""
class Project(models.Model):
    name = models.CharField(max_length=100)
    img = models.ImageField(upload_to='img')

    def __str__(self):
        return self.name


"""Model for Contact me on portfolio"""
class Contact(models.Model):
    name = models.CharField(max_length=100)
    client_email = models.EmailField()
    subject = models.CharField(max_length=255)
    message = models.TextField()
    my_address = models.CharField(max_length=255)
    my_phone = models.CharField(max_length=20)
    my_email = models.EmailField()

    class Meta:
        verbose_name = 'Contact'

    def __str__(self):
        return "Personal contact info"