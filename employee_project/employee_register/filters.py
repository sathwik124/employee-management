import django_filters
from django_filters import CharFilter
from .models import *

class OrderFilter(django_filters.FilterSet):
    fullname = CharFilter(field_name='fullname',lookup_expr='icontains')
    class Meta:
        model = Employee
        fields = '__all__'
        exclude = ['mobile','profile_pic']