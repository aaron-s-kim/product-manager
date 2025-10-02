from django.shortcuts import render
from django.db.models import Q
from .models import Product, Category, Tag


def product_list(request):
    products = Product.objects.all()
    categories = Category.objects.all()
    tags = Tag.objects.all()

    search_query = request.GET.get("search")
    if search_query:
        products = products.filter(
            Q(name__icontains=search_query) | Q(description__icontains=search_query)
        )

    category_filter = request.GET.get("category")
    if category_filter:
        products = products.filter(category_id=category_filter)
    
    tag_filters = request.GET.getlist("tags")
    if tag_filters:
        products = products.filter(tags__in=tag_filters).distinct()
        # distinct avoids duplicates if multiple tags match 1 product

    context = {
        "products": products,
        "categories": categories,
        "tags": tags,
        "search_query": search_query or "",
        "selected_category": category_filter or "",
        "selected_tags": [int(t) for t in tag_filters if t.isdigit()],
        # converts tag IDs to int list
    }

    return render(request, "products/product_list.html", context)
