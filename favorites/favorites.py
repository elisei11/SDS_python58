from decimal import Decimal

from django.conf import settings
from shop.models import Product


class Favorites:
    def __init__(self, request):
        self.session = request.session
        favorites = self.session.get(settings.FAVORITES_SESSION_ID)
        if not favorites:
            favorites = self.session[settings.FAVORITES_SESSION_ID] = {}
        self.favorites = favorites

    def add_to_favorites(self, product):
        """ add a product to favorites """

        product_id = str(product.id)
        if product_id not in self.favorites:
            self.favorites[product_id] = {

                'price': str(product.price),

            }
        # if override:
        #     self.favorites[product_id]['quantity'] = int(quantity)
        # else:
        #     self.favorites[product_id]['quantity'] += int(quantity)
        self.save()

    def save(self):
        self.session.modified = True

    def remove_from_favorites(self, product):
        product_id = str(product.id)
        if product_id in self.favorites:
            del self.favorites[product_id]
        self.save()

    def __iter__(self):
        product_ids = self.favorites.keys()
        products = Product.objects.filter(id__in=product_ids)
        favorites = self.favorites.copy()
        for product in products:
            favorites[str(product.id)]['product'] = product
        for item in favorites.values():
            item['price'] = Decimal(item['price'])
            # item['total_price'] = item['price'] * item['quantity']
            yield item

    # def __len__(self):
    #     return sum(item['quantity'] for item in self.cart.values())

    def clear(self):
        del self.session[settings.FAVORITES_SESSION_ID]
        self.save()

