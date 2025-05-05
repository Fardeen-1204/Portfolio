from django.shortcuts import render
from django.http import HttpResponse
from .models import ContactFormSubmission,About,info,made_projects

# Create your views here.
def home (request):
    about=About.objects.first()
    Info=info.objects.first()
    projects=made_projects.objects.all()
    context={'about':about,'info':Info,'projects':projects}
    return render(request, 'index.html',context)



def submit_contact_form(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        website = request.POST.get('website') == '1'
        ecommerce = request.POST.get('ecommerce') == '1'
        message = request.POST.get('message')

        ContactFormSubmission.objects.create(
            name=name,
            email=email,
            website=website,
            ecommerce=ecommerce,
            message=message
        )
        return HttpResponse("Thank you for your submission!")  # or redirect to a 'thank you' page
    else:
        return render(request, 'index.html')  # Replace with your actual form template
