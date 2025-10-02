from django.shortcuts import render
from django.db.models import Q
from .models import Product, Category


def product_list(request):
    products = Product.objects.all()
    categories = Category.objects.all()

    search_query = request.GET.get("search")
    if search_query:
        products = products.filter(
            Q(name__icontains=search_query) | Q(description__icontains=search_query)
        )

    category_filter = request.GET.get("category")
    if category_filter:
        products = products.filter(category_id=category_filter)

    context = {
        "products": products,
        "categories": categories,
        "search_query": search_query or "",
        "selected_category": category_filter or "",
    }

    return render(request, "products/product_list.html", context)
