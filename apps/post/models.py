from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse

from slugify import slugify
from .utils import get_time



User = get_user_model()


class Storage(models.Model):
    CATEGORY_CHOICES = (
        ('documents', 'Документ'),
        ('keys', 'Ключи'),
        ('technique', 'Техника'),
        ('wallets', 'Кошельки'),
        ('animals', 'Животные'),
        ('decorations', 'Украшения'),
        ('bags', 'Сумки'),
        ('other', 'Другое')
    )

    STATUS_CHOICES = (
        ('open', 'Открыто'),
        ('closed', 'Закрыто')
    )
    ADDRESS_CHOICES = (
        ('XXXXXX', 'xxxxxx'),
        ('YYYYYY', 'yyyyyy')
    )
    STORAGE_CHOICES = (
        ('lost', 'Потерял'),
        ('find', 'Нашел')
    )
    storage = models.CharField(
        max_length=20,
        choices=STORAGE_CHOICES
    )
    # storage = models.ForeignKey(
    #     choices=STORAGE_CHOICES,
    #     to='self',
    #     on_delete=models.CASCADE,
    #     related_name='storages',
    #     blank=True,
        # choices=STORAGE_CHOICES,
    # )
    user = models.ForeignKey(
        verbose_name='Автор поста',
        to=User,
        on_delete=models.CASCADE,
        related_name='publication'
    )
    title = models.CharField(verbose_name='Что вы нашли?', max_length=200)
    slug = models.SlugField(max_length=170, primary_key=True, blank=True)
    image = models.ImageField(upload_to='find_images')
    status = models.CharField(
        max_length=15,
        choices=STATUS_CHOICES,
        
    )
    text = models.TextField()
    category = models.CharField(
        max_length=100,
        choices=CATEGORY_CHOICES
    )
    address = models.CharField(max_length=100, choices=ADDRESS_CHOICES)
    date = models.DateField(verbose_name='Дата находки')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title + get_time())

        super().save(*args, **kwargs)


    class Meta:
        ordering = ('created_at',)

    def get_absolute_url(self):
        return reverse("post-detail", kwargs={"pk": self.pk})








# class ProductViewSet(ModelViewSet):
#     queryset = Product.objects.filter(in_stock=True)
# product.object.filter(in_stock=True)
