from ..models import Review, Product, UserAccount


class reviews:
    def addReview(self, account_id, product_id, stars, feedback):
        product = Product.objects.get(pk=product_id)
        account = UserAccount.objects.get(pk=account_id)
        review = Review(stars=stars, feedback=feedback,
                        product=product, user=account)
        review.save()
