from .category import category


class categories:
    def all(self):
        return category.all()

    def get(self, *args, **kwargs):
        return category.get(args, kwargs)

    def filter(self, *args, **kwargs):
        return category.filter(args, kwargs)

    def addCategory(self, category_name):
        try:
            c = category(name=category_name)
            c.save()
        except:
            raise Exception("Couldn't Add Category")
