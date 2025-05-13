from django.db import models

class MenuItem(models.Model):
    name = models.CharField(max_length=100, verbose_name="Назва")
    description = models.TextField(blank=True, verbose_name="Опис")
    price = models.DecimalField(
        max_digits=7, 
        decimal_places=2, 
        verbose_name="Ціна"
    )
    # якщо хочеш зберігати зображення через модель, інакше просто використовуй статичні файли
    image = models.ImageField(
        upload_to='menu_images/', 
        blank=True, 
        null=True, 
        verbose_name="Картинка"
    )

    def __str__(self):
        return self.name