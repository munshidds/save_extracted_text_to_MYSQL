from django.shortcuts import render
from .models import CustomerImage
import cv2
import pytesseract


def upload_image(request):
    if request.method == 'POST':
        customer_name = request.POST['customer_name']
        image = request.FILES['image']
        filename = image.name

        # Save the uploaded image to a temporary file (you may need to install the 'Pillow' library for this)
        with open(filename, 'wb') as temp_file:
            for chunk in image.chunks():
                temp_file.write(chunk)

        # Read the image using OpenCV
        image_ = cv2.imread(filename)

        # Use Tesseract to extract text
        extracted_text = pytesseract.image_to_string(image_)

        CustomerImage.objects.create(customer_name=customer_name, image=image,extracted_text=extracted_text)
    return render(request, 'upload.html')


def display_image(request):
    images = CustomerImage.objects.all()
    return render(request, 'display_image.html', {'images': images})


