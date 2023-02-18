from django.views import View
from django.conf import settings
from django.http import JsonResponse
from django.views.generic import TemplateView 
import stripe
from .models import Product
from django.views.generic.list import ListView


stripe.api_key = settings.STRIPE_SECRET_KEY


# class AllProductdsView(TemplateView):
#     template_name = 'products.html',
    


class SuccessView(TemplateView):
    template_name = 'success.html'

class CancelView(TemplateView):
    template_name = 'cancel.html'


class ProductListView(ListView):
    model = Product
    template_name = 'products.html'

class ProductLandingPageView(TemplateView):
    template_name = 'index.html'
    def get_context_data(self, **kwargs):
        product = Product.objects.get(id=self.kwargs['pk'])
        context =  super(ProductLandingPageView, self).get_context_data(**kwargs)
        context.update({
            'product': product,
            'STRIPE_PUBLIC_KEY': settings.STRIPE_PUBLIC_KEY
        })
        return context



class CreateCheckoutSessionView(View):
    def post(self, request, *args, **kwargs):
        product_id = self.kwargs['id']
        product = Product.objects.get(id = product_id)
        print(product)
        DOMAIN = 'http://127.0.0.1:8000'
        checkout_session = stripe.checkout.Session.create(
            payment_method_types = ['card'],
            line_items = [
            {
                'price_data' : {
                    'currency': 'usd',
                    'unit_amount': product.price,
                    'product_data': {
                        'name': product.name,
                        #'images': ['https://i.imgur.com/EHyR2nP.png']
                    },

                },
                'quantity': 1
            },
            ],

            mode = 'payment', 
            success_url = DOMAIN + '/success',
            cancel_url = DOMAIN + '/cancel'
        )
        return JsonResponse({
            'id': checkout_session.id
        })