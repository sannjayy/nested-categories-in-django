from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField()
    parent = models.ForeignKey('self', blank=True, null=True, related_name='children', on_delete=models.CASCADE)

    class Meta:
        unique_together = ('slug', 'parent',)  
        verbose_name_plural = "categories"    

    def __str__(self):
        path = [f'{self.name} (#{self.id})']
        parent = self.parent
        while parent is not None:
            path.append(f'{parent.name} (#{parent.id})')
            parent = parent.parent
        return ' > '.join(path[::-1])


class Product(models.Model):
    name = models.CharField(max_length=100)
    category = models.ManyToManyField(Category)

    def __str__(self):
        return self.name

    @property
    def get_category(self):
        return " | ".join(d.name for d in self.category.all())