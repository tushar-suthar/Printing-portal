from django.shortcuts import render
import razorpay
from .forms import UploadFileForm
from django.views.decorators.csrf import ensure_csrf_cookie

# Create your views here.
def home(request):
    if request.method =='POST':
#get name and amount from post form in home.html

        name=request.POST.get("name")
        amount=int(request.POST.get("amount"))*100
        client= razorpay.Client(
            auth=('rzp_test_n3qH2GsBpebh9L','Bds7rwGHjsRDVUFDjPFKQLHx')
        )
        payment=client.order.create({'amount':amount,'currency':'INR','payment_capture':'1'})
        return render(request,'home.html',{'payment':payment})

        # OPTIONALclient.order.create(amount=order_amount, currency=order_currency, receipt=order_receipt, notes=notes)
    return render(request,'home.html')

def success(request):
    return render(request,'success.html')




# pdf upload handling

@ensure_csrf_cookie
def upload_multiple_files(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        files = request.FILES.getlist('files')
        if form.is_valid():
            for f in files:
                handle_uploaded_file(f)
            context = {'msg' : '<span style="color: green;">File successfully uploaded</span>'}
            return render(request, "fileupload.html", context)
    else:
        form = UploadFileForm()
    return render(request, 'fileupload.html', {'form': form})

def handle_uploaded_file(f):
    with open(f.name, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)