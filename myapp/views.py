from django.shortcuts import render
from .models import CustomerImage

def upload_image(request):
    if request.method == 'POST':
        customer_name = request.POST['customer_name']
        image = request.FILES['image']
        CustomerImage.objects.create(customer_name=customer_name, image=image)
    return render(request, 'upload.html')
