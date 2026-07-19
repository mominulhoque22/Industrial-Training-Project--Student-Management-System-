from rest_framework import serializers

def validate_salary(value):
    if value < 0:
        raise serializers.ValidationError("salary must be a positive number.")
    return value