import django_filters 
from ..models import Tool

class ToolFilter(django_filters.FilterSet):

    OPTIONS = (
        ('ascending', 'Mais Barato'),
        ('descending', 'Mais Caro'),
        ('a_first', 'A a Z'),
        ('z_first', 'Z a A'),
    )

    ordering = django_filters.ChoiceFilter(label='Ordenar Por:', choices=OPTIONS, method='filter_by_order',)

    def filter_by_order(self, queryset, name, value):

        if value == 'ascending' :
            expression = 'price'
        elif value == 'descending' :
            expression = '-price'
        elif value == 'a_first' :
            expression = 'name'
        elif value == 'z_first' :
            expression = '-name'

        return queryset.order_by(expression)
