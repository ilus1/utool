import django_filters 
from .models import Tool

class ToolFilter(django_filters.FilterSet):

    CHOICES = (
        ('ascending', 'Mais Barato'),
        ('descending', 'Mais Caro')
    )

    ordering = django_filters.ChoiceFilter(label='Ordenar Por:', choices=CHOICES, method='filter_by_order',)

    class Meta:
        model = Tool
        fields = {
            'name': ['icontains'],
        }

    def filter_by_order(self, queryset, name, value):

        expression = 'price' if value == 'ascending' else '-price'

        return queryset.order_by(expression)
