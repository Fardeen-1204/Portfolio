from django.db import models
from django.core.exceptions import ValidationError
# Create your models here.


class ContactFormSubmission(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    website = models.BooleanField(default=False)
    ecommerce = models.BooleanField(default=False)
    message = models.TextField(blank=True)

    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.email}"


class About(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.pk and About.objects.exists():
            raise ValidationError("Only one About instance is allowed.")
        super().save(*args, **kwargs)


class info(models.Model):
    exp=models.IntegerField()
    customer=models.IntegerField()
    projects=models.IntegerField()

    def __str__(self):
        return f'{self.exp} - {self.customer}'

    def save(self, *args, **kwargs):
        if not self.pk and info.objects.exists():
            raise ValidationError("Only one About instance is allowed.")
        super().save(*args, **kwargs)

class made_projects(models.Model):
    title=models.CharField(max_length=100)
    description=models.TextField()
    image=models.ImageField(upload_to='images/')
    link=models.URLField(null=False)

    def __str__(self):
        return self.title