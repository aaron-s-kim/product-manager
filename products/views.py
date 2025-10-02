from django.shortcuts import render
from django.db.models import Q
from .models import Product


def product_list(request):
    products = Product.objects.all()

    search_query = request.GET.get("search")
    if search_query:
        products = products.filter(
            Q(name__icontains=search_query) | Q(description__icontains=search_query)
        )

    context = {
        "products": products,
        "search_query": search_query or "",
    }

    return render(request, "products/product_list.html", context)
