import factory
import factory.fuzzy

from ..models import Category, Tool
from ..models import MyUserModel


class UserFactory(factory.django.DjangoModelFactory):
    username = factory.fuzzy.FuzzyText()
    name = factory.fuzzy.FuzzyText()
    cpf = factory.fuzzy.FuzzyText()
    email = factory.fuzzy.FuzzyText()
    password = factory.fuzzy.FuzzyText()

    class Meta:
        model = MyUserModel

class CategoryFactory(factory.django.DjangoModelFactory):
    name = factory.fuzzy.FuzzyText()

    class Meta:
        model = Category


class ToolFactory(factory.django.DjangoModelFactory):
    category = factory.SubFactory(CategoryFactory)
    name = factory.fuzzy.FuzzyText()
    image = factory.django.ImageField()
    description = factory.Faker("paragraph", nb_sentences=3, variable_nb_sentences=True)
    price = factory.fuzzy.FuzzyDecimal(5.0, 999.99)
    is_available = factory.Faker("pybool")
    owner = factory.SubFactory(UserFactory)

    class Meta:
        model = Tool