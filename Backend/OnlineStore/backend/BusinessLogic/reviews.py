from ..models import Review


class reviews:
    def addReview(self, account, product, stars, feedback):
        review = Review(stars=stars, feedback=feedback,
                        product=product, user=account)
        review.save()
