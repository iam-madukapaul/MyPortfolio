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
    link = models.URLField(blank=True)

    def __str__(self):
        return self.name


"""Model for MyInfo on portfolio"""
class MyInfo(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    my_details = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        verbose_name = 'myinfo'
        verbose_name_plural = 'myinfo'

    def __str__(self):
        return "Personal contact info"


"""Model for Contact me on portfolio"""
class Contact(models.Model):
    name = models.CharField(max_length=100)
    client_email = models.EmailField()
    subject = models.CharField(max_length=255)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True , null=True, blank=True)

    class Meta:
        verbose_name = 'Contact'
        verbose_name_plural = 'contacts'

    def __str__(self):
        return self.name + '' + self.client_email