from rest_framework import serializers
from .models import Restaurant, Menu, Employee


class RestaurantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurant
        fields = ('id', 'name', 'address', 'phone_number', 'created_at', 'updated_at')


class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = '__all__'


class EmployeeSerializer(serializers.ModelSerializer):
    voted_menu = MenuSerializer(many=False, read_only=True)

    class Meta:
        model = Employee
        fields = ('id', 'name', 'build_version', 'voted_menu')
