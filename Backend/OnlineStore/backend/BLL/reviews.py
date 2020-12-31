from .review import review


class reviews:

    def all(self):
        return review.all()

    def get(self, *args, **kwargs):
        return review.get(*args, **kwargs)

    def filter(self, *args, **kwargs):
        return review.filter(*args, **kwargs)

    def addReview(self, buyer, product, stars, feedback):
        r = review(stars=stars, feedback=feedback,
                   product=product.data, buyer=buyer.data)
        r.save()
