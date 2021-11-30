from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request, 'index.html', {})


def search(request):
    if request.method == 'POST':
        searched = request.POST['searched']
        product = Product.objects.filter(name__contains=searched)
        supplier = Supplier.objects.filter(name__contains=searched)
        return render(request, 'product/search_product.html', {'searched': searched, 'product': product, 'supplier': supplier})
    else:
        return render(request, 'product/search_product.html', {})


def dashboard(self):
    return reverse('index', {})
