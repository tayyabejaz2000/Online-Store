from .categories import categories
from .reviews import reviews
from .product import product
from .seller import seller
from .product import product


class products:
    def __init__(self):
        self.categories = categories()
        self.reviews = reviews()

    def all(self):
        return product.all()

    def get(self, *args, **kwargs):
        return product.get(*args, **kwargs)

    def filter(self, *args, **kwargs):
        return product.filter(*args, **kwargs)

    def addProduct(self, product_name, product_desc, quantity, price, discount, category_name, seller: seller):
        try:
            categ = self.categories.get(pk=category_name)
            p = product(name=product_name, description=product_desc,
                        stock=quantity, price=price, discount=discount, shop=seller.shop.data, category=categ)
            p.save()
        except:
            raise Exception("Couldn't add Product for Shop, [Product Name]:" + str(product_name) +
                            ", [Product Description]:" + str(product_desc) + ", [Quantity]:" + str(quantity))

    def removeProduct(self, product_id):
        try:
            prod = product(self.get(pk=product_id))
            prod.removeProduct()
        except:
            raise Exception("Couldn't remove Product: [Product ID]:" +
                            str(product_id))

    def updateProduct(self, product_id, product_name, product_description, product_stock, product_price, product_discount, product_category_name):
        prod = product(self.get(pk=product_id))
        product_category = self.categories.get(pk=product_category_name)
        prod.update(product_name, product_description, product_stock,
                    product_price, product_discount, product_category)

    def addReview(self, buyer, prod, stars, feedback):
        self.reviews.addReview(buyer, prod, stars, feedback)

    def addCategory(self, category_name):
        self.categories.addCategory(category_name)
