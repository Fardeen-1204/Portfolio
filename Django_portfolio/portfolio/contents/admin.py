from django.contrib import admin
from .models import ContactFormSubmission,About,info,made_projects

# Register your models here.
admin.site.register(ContactFormSubmission)
admin.site.register(About)
admin.site.register(info)
admin.site.register(made_projects)