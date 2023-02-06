import re
from rest_framework import serializers
from .models import Client


def validate_first_digit(value: [str]) -> int:
    count = 10
    _sum = 0
    for digit in value:
        if count >= 2:
            _sum += int(digit) * count
            count -= 1
    result = (_sum * 10) % 11
    return 0 if result == 10 else result


def validate_second_digit(value: [str]) -> int:
    count = 11
    _sum = 0
    for digit in value:
        if count >= 2:
            _sum += int(digit) * count
            count -= 1
    result = (_sum * 10) % 11
    return 0 if result == 10 else result


class ClientSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    cpf = serializers.CharField(max_length=14, min_length=11)
    name = serializers.CharField(max_length=100)
    birth_date = serializers.DateField()
    created_at = serializers.DateTimeField(read_only=True)
    updated_at = serializers.DateTimeField(read_only=True)

    def validate_cpf(self, value):
        value = re.sub(r'\W', '', value)

        if len(value) != 11:
            raise serializers.ValidationError(f'CPF inválido')

        first_digit = validate_first_digit(value)
        if first_digit != int(value[9]):
            raise serializers.ValidationError('CPF inválido')

        second_digit = validate_second_digit(value)
        if second_digit != int(value[10]):
            raise serializers.ValidationError('CPF inválido')

        return value

    def create(self, validated_data):
        cpf = re.sub(r'\W', '', validated_data.get('cpf'))
        if Client.objects.filter(cpf__exact=cpf).exists():
            raise serializers.ValidationError("Cpf ja cadastrado!")
        client = Client(**validated_data)
        client.save()
        return client

    class Meta:
        model = Client
        fields = '__all__'
