from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required, user_passes_test
from django.views.decorators.csrf import csrf_exempt
from .models import Product
import json


# ----------------------------
# NORMAL TEMPLATE VIEWS
# ----------------------------

def product_list(request):
    products = Product.objects.all()
    return render(request, 'products.html', {'products': products})


def is_admin(user):
    return user.is_staff


@login_required
@user_passes_test(is_admin)
def add_product(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        price = request.POST.get('price')
        image = request.FILES.get('image')

        Product.objects.create(
            title=title,
            price=price,
            image=image
        )
        return redirect('product_list')

    return render(request, 'add_product.html')


@login_required
@user_passes_test(is_admin)
def edit_product(request, id):
    product = get_object_or_404(Product, id=id)

    if request.method == 'POST':
        product.title = request.POST.get('title')
        product.price = request.POST.get('price')

        if request.FILES.get('image'):
            product.image = request.FILES.get('image')

        product.save()
        return redirect('product_list')

    return render(request, 'edit_product.html', {'product': product})


@login_required
@user_passes_test(is_admin)
def delete_product(request, id):
    product = get_object_or_404(Product, id=id)
    product.delete()
    return redirect('product_list')


# ----------------------------
# API VIEWS (FOR POSTMAN)
# ----------------------------

def product_api_list(request):
    products = Product.objects.all()
    data = []

    for p in products:
        data.append({
            "id": p.id,
            "title": p.title,
            "price": p.price,
            "image": p.image.url if p.image else None
        })

    return JsonResponse(data, safe=False)


@csrf_exempt
def product_api_create(request):
    if request.method == "POST":
        data = json.loads(request.body)

        product = Product.objects.create(
            title=data.get("title"),
            price=data.get("price")
        )

        return JsonResponse({
            "message": "Product created",
            "id": product.id
        })

    return JsonResponse({"error": "Invalid request"}, status=400)


@csrf_exempt
def product_api_delete(request, id):
    if request.method == "DELETE":
        product = get_object_or_404(Product, id=id)
        product.delete()

        return JsonResponse({"message": "Product deleted"})

    return JsonResponse({"error": "Invalid request"}, status=400)