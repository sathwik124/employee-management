from rest_framework import serializers
from employee_register.models import Employee

class RegSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'
