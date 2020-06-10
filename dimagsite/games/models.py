from django.db import models
from datetime import date

class Category(models.Model):
    """Категории"""
    name = models.CharField("Категория", max_length=150)
    description = models.TextField("Описание")
    url = models.SlugField(max_length=160, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

class Creators(models.Model):
    """Создатели"""
    name = models.CharField("Имя", max_length=150)
    age = models.PositiveSmallIntegerField("Возраст", default=0)
    description = models.TextField("Описание")
    immage = models.ImageField("Изображение", upload_to="creators/")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Создатели и програмисты"
        verbose_name_plural = "Создатели"

class Genre(models.Model):
    """Жанр"""
    name = models.CharField("Название", max_length=150)
    description = models.TextField("Описание")
    url = models.SlugField(max_length=160, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Жанр"
        verbose_name_plural = "Жанры"

class Game(models.Model):
    """Игры"""
    title = models.CharField("Название", max_length=150)
    tagline = models.CharField("Слоган", max_length=100, default='')
    year = models.PositiveSmallIntegerField("Возраст", default=1989)
    russia_year = models.DateField("Выход в РФ", default=date.today)
    countru = models.CharField("Страна", max_length=30)
    genres = models.ManyToManyField(Genre, verbose_name='Жанры')
    description = models.TextField("Описание")
    poster = models.ImageField("Изображение", upload_to="posters/")
    creators = models.ManyToManyField(Creators, verbose_name="Создатель", related_name="game_creator")
    category = models.ForeignKey(
        Category, verbose_name="Категория", on_delete=models.SET_NULL, null=True
        )
    url = models.SlugField(max_length=160, unique=True)
    draft = models.BooleanField("Черновик", default=False)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Игра"
        verbose_name_plural = "Игры"

class Screansoots(models.Model):
    """Кадры"""
    title = models.CharField("Заголовок", max_length=100)
    description = models.TextField("Описание")
    immage = models.ImageField("Изображение", upload_to="screan_soots/")
    game = models.ForeignKey(Game, verbose_name="Создатель", on_delete=models.CASCADE)
    url = models.SlugField(max_length=160, unique=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Кадр"
        verbose_name_plural = "Кадры"

class Reviews(models.Model):
    """Отзыв"""
    email = models.EmailField()
    name = models.CharField("Имя", max_length=100)
    text = models.TextField("Сообщение", max_length=5000)
    parent = models.ForeignKey(
        'self', verbose_name="Родитель", on_delete=models.SET_NULL, blank=True, null=True
    )
    game = models.ForeignKey(Game, verbose_name="фильм", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name} - {self.game}"

    class Meta:
        verbose_name = "Отзыв"
        verbose_name_plural = "Отзывы"
            