from django.db import models


class Phone(models.Model):
    # TODO: Добавьте требуемые поля.
    #  В файле models.py нашего приложения создаем модель Phone с полями
    #  id, name, price, image, release_date, lte_exists и slug.
    #  Поле id - должно быть основным ключом модели.

    name = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=7, decimal_places=2)
    image = models.ImageField()
    release_date = models.DateField()
    lte_exists = models.BooleanField()
    slug = models.SlugField(null=True)
