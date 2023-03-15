import json

from django.http import JsonResponse
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import DetailView

from ads.models import Category, Ads


def index(request) -> JsonResponse:
    """
     The index function is a representation that processes a GET request to the root domain. Takes a request object
     as an argument and returns a message in JSON format.
    """
    return JsonResponse({"status": "ok"}, status=200)


@method_decorator(csrf_exempt, name='dispatch')
class CategoriesView(View):
    """
    The CategoriesView class inherits from the View class from the django module and is a class-based view
    for processing requests by GET and POST methods at the address '/cat/'.
    """
    def get(self,request) -> JsonResponse:
        """
        The get function is a class-based view method for processing a GET request at the address '/cat/'.
        Takes a request object as an argument. Makes a query from the database of all values and returns
        the result in the form of JSON.
        """
        categories = Category.objects.all()
        response = []
        for category in categories:
            response.append({
                "id": category.id,
                "name": category.name
            })
        return JsonResponse(response, safe=False, json_dumps_params={"ensure_ascii": False})

    def post(self, request) -> JsonResponse:
        """
        The post function is a class-based view method for processing a POST request at the address '/cat/'.
        Designed to add a new object to the database. Takes a request object as an argument.
        Retrieves the data of a new object from the request body, generates and stores the object in the database.
        Returns the saved object as JSON.
        """
        category_data = json.loads(request.body)
        category = Category()
        category.name = category_data["name"]

        category.save()

        response = {
                "id": category.id,
                "name": category.name
        }
        return JsonResponse(response)


@method_decorator(csrf_exempt, name='dispatch')
class AdsView(View):
    """
    The AdsView class inherits from the View class from the django module and is a class-based view
    for processing requests by GET and POST methods at the address '/ad/'.
    """
    def get(self, request) -> JsonResponse:
        """
        The get function is a class-based view method for processing a GET request at the address '/ad/'.
        Takes a request object as an argument. Makes a query from the database of all values and returns
        the result in the form of JSON.
        """
        ads = Ads.objects.all()
        response = []
        for ad in ads:
            response.append({
                "id": ad.id,
                "name": ad.name,
                "author": ad.author,
                "price": ad.price
            })
        return JsonResponse(response, safe=False, json_dumps_params={"ensure_ascii": False})

    def post(self, request) -> JsonResponse:
        """
        The post function is a class-based view method for processing a POST request at the address '/ad/'.
        Designed to add a new object to the database. Takes a request object as an argument.
        Retrieves the data of a new object from the request body, generates and stores the object in the database.
        Returns the saved object as JSON.
        """
        ad_data = json.loads(request.body)
        print(type(ad_data["price"]))
        ad = Ads()
        ad.name = ad_data["name"],
        ad.price = 0,    # ad_data["price"],
        ad.description = ad_data["description"],
        ad.author = ad_data["author"],
        ad.address = ad_data["address"],

        ad.save()

        response = {
            "id": ad.id,
            "name": ad.name,
            "author": ad.author,
            "description": ad.description,
            "address": ad.address,
            "is_published": ad.is_published,
            "price": ad.price
        }

        return JsonResponse(response)


class CategoryDetailView(DetailView):
    """
    The CategoryDetailView class inherits from the DetailView class from the django generic module and is
    a class-based view for processing requests with GET methods at the address '/cat/<int: pk>'.
    """
    model = Category
    def get(self, request, *args, **kwargs) -> JsonResponse:
        """
        The get function is a class-detail view method for processing a GET request at the address '/cat/<int:pk>'.
        Designed to get detailed data about the requested object. Takes a request object as an argument.
        Returns the result as JSON.
        """
        category = self.get_object()
        response = {"id": category.id, "name": category.name}
        return JsonResponse(response, json_dumps_params={"ensure_ascii": False})


class AdDetailView(DetailView):
    """
    The AdDetailView class inherits from the DetailView class from the django generic module and is
    a class-based view for processing requests with GET methods at the address '/ad/<int: pk>'.
    """
    model = Ads

    def get(self, request, *args, **kwargs) -> JsonResponse:
        """
        The get function is a class-detail view method for processing a GET request at the address '/ad/<int:pk>'.
        Designed to get detailed data about the requested object. Takes a request object as an argument.
        Returns the result as JSON.
        """
        ad = self.get_object()
        response = {"id": ad.id,
                    "name": ad.name,
                    "author": ad.author,
                    "price": ad.price,
                    "description": ad.description,
                    "address": ad.address,
                    "is_published": ad.is_published}
        return JsonResponse(response, json_dumps_params={"ensure_ascii": False})
