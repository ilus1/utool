from autoslug import AutoSlugField
from django.db import models
from django.urls import reverse
from model_utils.models import TimeStampedModel
from users.models import MyUserModel

class AvailableManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_available=True)

class Category(TimeStampedModel):
    name = models.CharField(
        max_length=255, 
        unique=True
    )
    slug = AutoSlugField(
        unique=True, 
        always_update=False, 
        populate_from="name"
    )

    class Meta:
        ordering = ("name",)
        verbose_name = "category"
        verbose_name_plural = "categories"

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("pages:list_by_category", kwargs={"slug": self.slug})

class Tool(TimeStampedModel):
    category = models.ForeignKey(
        Category, related_name="tools", 
        on_delete=models.CASCADE,
        verbose_name='Categoria da Ferramenta',
    )
    name = models.CharField(
        max_length=255,
        verbose_name='Nome da Ferramenta'
    )
    slug = AutoSlugField(
        unique=True, 
        always_update=False, 
        populate_from="name"
    )
    image = models.ImageField(
        upload_to="tools/%Y/%m/%d", 
        blank=True,
        verbose_name='Imagem',
        default='/tools/2021/03/16/default_tool.jpg'
    )
    description = models.TextField(
        max_length=500,
        blank=True,
        verbose_name='Descrição'
    )
    price = models.DecimalField(
        max_digits=10, 
        decimal_places=2,
        verbose_name='Preço'
    )
    is_available = models.BooleanField(
        default=True,
        verbose_name='Disponível'
    )
    owner = models.ForeignKey(
        MyUserModel, 
        on_delete=models.CASCADE
    )

    objects = models.Manager()
    available = AvailableManager()

    class Meta:
        ordering = ("name",)


    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("pages:detail", kwargs={"slug": self.slug})
    

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)


class ToolDisposableParts(Tool):
    disposable_parts = models.CharField(
        max_length=10, 
        choices=(
            ('Lixa', 'Lixa'),
            ('Broca', 'Broca'),
            ('Serra', 'Serra'),
            ('Lâmina', 'Lâmina'),
        ), 
        verbose_name="Partes desgastáveis",
    )

    disposable_part_price = models.DecimalField(
        max_digits=10, 
        decimal_places=2, 
        verbose_name="Preço da parte desgastável"
    )

class ToolWrench(Tool):
    size = models.PositiveIntegerField(
        verbose_name = "Tamanho"
    )

class ToolEletric(Tool):
    voltage = models.CharField(
        max_length=6, 
        choices=(
            ('110V', '110V'),
            ('220V', '220V'),
            ('Bivolt', 'Bivolt'),
        ),
        verbose_name="Voltagem"
    )
    
    extra_part = models.CharField(
        max_length=500,
        blank=True,
        verbose_name="Parte extra"
    )
    
    extra_part_specification = models.TextField(
        blank=True,
        verbose_name="Expecificação da parte extra",
    )
