from .reviews import reviews
from ..models import Category, Product
from .product import product


class products:
    def __init__(self):
        self.reviews = reviews()

    def all(self):
        return product.all()

    def get(self, *args, **kwargs):
        return product.get(args, kwargs)

    def filter(self, *args, **kwargs):
        return product.filter(args, kwargs)

    def addProduct(self, product_name, product_desc, quantity, category, shop, price):
        try:
            _category = self.getCategory(category)
            product = Product(name=product_name, description=product_desc,
                              stock=quantity, shop=shop, category=_category, price=price)
            product.save()
        except:
            raise Exception("Couldn't add Product for Shop, [Product Name]:" + str(product_name) +
                            ", [Product Description]:" + str(product_desc) + ", [Quantity]:" + str(quantity))

    def removeProduct(self, product_id):
        try:
            product = self.getProduct(product_id)
            product.isRemoved = True
            product.save()
        except:
            raise Exception("Couldn't delete Product: [Product ID]:" +
                            str(product_id))

    def getAllProducts(self):
        return list(Product.objects.filter(isRemoved=False))

    def updateProduct(self, product_id, product_name, product_desc, product_quantity, category, price):
        try:
            product = self.getProduct(product_id)
            product.name = product_name
            product.description = product_desc
            product.stock = product_quantity
            product.category = self.getCategory(category)
            product.price = price
            product.save()
        except:
            raise Exception("Couldn't update Product for Shop, [Product Name]:" + str(product_name) +
                            ", [Product Description]:" + str(product_desc) + ", [Quantity]:" + str(product_quantity))

    # adan

    def addReview(self, account, product, stars, feedback):
        self.reviews.addReview(account, product, stars, feedback)
