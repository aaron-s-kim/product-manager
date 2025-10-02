from django.core.management.base import BaseCommand
from products.models import Category, Tag, Product
from decimal import Decimal
import random


class Command(BaseCommand):

    def handle(self, *args, **options):
        print("Loading sample data...")

        # Create categories
        cats = [
            ("Electronics", "Phones, laptops, gadgets"),
            ("Clothing", "Shirts, pants, shoes"),
            ("Books", "Fiction, tech books, etc"),
            ("Home", "Kitchen, furniture, decor"),
            ("Sports", "Equipment and gear"),
        ]

        categories = []
        for name, desc in cats:
            cat, _ = Category.objects.get_or_create(
                name=name, defaults={"description": desc}
            )
            categories.append(cat)

        # Create tags
        tags = []
        tag_data = [
            ("Popular"),
            ("Sale"),
            ("New"),
            ("Premium"),
            ("Budget"),
            ("Wireless"),
            ("Eco"),
            ("Limited"),
            ("Bestseller"),
            ("Featured"),
        ]

        for tag_name in tag_data:
            tag, _ = Tag.objects.get_or_create(name=tag_name)
            tags.append(tag)

        # Create products
        products = [
            (
                "iPhone 15 Pro",
                "Latest Apple smartphone with titanium design",
                1199.00,
                categories[0],
            ),
            ("MacBook Air M3", "13-inch laptop with M3 chip", 1099.00, categories[0]),
            (
                "AirPods Pro",
                "Wireless earbuds with noise cancellation",
                249.00,
                categories[0],
            ),
            ("Samsung 4K TV", "55-inch smart TV with HDR", 699.00, categories[0]),
            ("Gaming Mouse", "RGB gaming mouse with 12000 DPI", 79.99, categories[0]),
            ("Nike Air Max", "Comfortable running shoes", 129.99, categories[1]),
            ("Levi's 501 Jeans", "Classic straight leg jeans", 89.99, categories[1]),
            ("Plain White Tee", "Basic cotton t-shirt", 19.99, categories[1]),
            ("Wool Sweater", "Cozy winter sweater", 65.00, categories[1]),
            ("Baseball Cap", "Adjustable sports cap", 24.99, categories[1]),
            ("Clean Code", "Programming best practices book", 45.99, categories[2]),
            ("Django Tutorial", "Web development with Django", 39.99, categories[2]),
            ("Sci-Fi Novel", "Space adventure story", 16.99, categories[2]),
            ("Cook Book", "Easy recipes for beginners", 29.99, categories[2]),
            ("History Book", "World War II stories", 34.99, categories[2]),
            ("Coffee Machine", "Automatic espresso maker", 299.99, categories[3]),
            ("Table Lamp", "Modern LED desk lamp", 59.99, categories[3]),
            ("Throw Pillow", "Decorative couch pillow", 24.99, categories[3]),
            ("Basketball", "Official size and weight", 39.99, categories[4]),
            ("Yoga Mat", "Non-slip exercise mat", 29.99, categories[4]),
        ]

        for name, desc, price, cat in products:
            qty = random.randint(10, 100)

            product, created = Product.objects.get_or_create(
                name=name,
                defaults={
                    "description": desc,
                    "price": Decimal(str(price)),
                    "category": cat,
                    "quantity": qty,
                },
            )

            if created:
                # randomly assign 1-3 tags to each product
                num_tags = random.randint(1, 3)
                product_tags = random.sample(tags, num_tags)
                product.tags.set(product_tags)

        print("Done! Added 5 categories, 10 tags, and 20 products")
