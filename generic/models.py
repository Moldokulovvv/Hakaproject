from django.db import models


from account.models import User


class Category(models.Model):

    slug = models.SlugField(primary_key=True, max_length=50)
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to='categories', blank=True)

    def __str__(self):
        return self.name

class Ticket(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField()
    location = models.TextField()
    time = models.TimeField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='tickets')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tickets')
    created = models.DateTimeField()
    image = models.ImageField(upload_to='tickets')


    def __str__(self):
        return self.title










