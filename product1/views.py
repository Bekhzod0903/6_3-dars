from django.shortcuts import render
from .models import Product,Category
# Create your views here.



def get_info(request):
    categories = Category.objects.all()
    context = {
        'categories': categories

    }
    return render(request, 'index.html',context=context)


def get_product(request,pk):
    product = Product.objects.get(pk=pk)
    context = {
        'product': product
    }
    return render(request, 'product.html', context=context)