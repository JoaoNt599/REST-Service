from functools import wraps
from rest_framework import serializers
from core.models import PontoTuristico
import re


def required_and_not_numeric(field_name="este campo"):
    def decorator(func):
        @wraps(func)
        def wrapper(self, value):
            if not value.strip():
                raise serializers.ValidationError(f"O campo '{field_name}' é obrigatório.")
            if not re.search('[a-zA-Z]', value):
                raise serializers.ValidationError(f"O compo '{field_name}' não pode conter apenas números.")
            return func(self, value)
        return wrapper
    return decorator


def unique_validation(model, fields):
    def decorator(func):
        @wraps(func)
        def wrapper(self, data):
            filter_kwargs = {field: data.get(field) for field in fields}
            if model.objects.filter(**filter_kwargs).exists():
                field_names = ', '.join(fields)
                raise serializers.ValidationError(f"Já existe um registro com os campos ({field_names}) informados.")
            return func(self, data)
        return wrapper
    return decorator


def min_length_field(min_length, message=None):
    def decorator(func):
        @wraps(func)
        def wrapper(self, value):
            if len(value.strip()) < min_length:
                raise serializers.ValidationError(message or f"O campo deve ter pelo meno {min_length} caracteres.")
            return func(self, value)
        return wrapper
    return decorator


def validate_put_fields(model, unique_fields):
    def decorator(method):
        @wraps(method)
        def wrapper(self, instance, validated_data):
            field_errors = {}

            # Validação de campos nulos ou somente numéricos
            for field, value in validated_data.items():
                if isinstance(value, str):
                    if not value.strip():
                        field_errors[field] = f"O campo '{field}' é obrigatório."
                    if not re.search('[a-zA-Z]', value):
                        field_errors[field] = f"O campo '{field}' não pode conter apenas números."

            # Validação individual de cada campo 
            for field in unique_fields:
                new_value = validated_data.get(field)
                if new_value:
                    exists = model.objects.filter(**{field: new_value}).exclude(pk=instance.pk).exists()
                    if exists:
                        field_errors[field] = f"Já existe um registro com esse valor para o campo '{field}'."

            # Validação combinada de todos os campos juntos
            if all(field in validated_data for field in unique_fields):
                combo_filter = {field: validated_data[field] for field in unique_fields}
                exists_combo = model.objects.filter(**combo_filter).exclude(pk=instance.pk).exists()
                if exists_combo:
                    field_list = ', '.join(unique_fields)
                    if "non_field_errors" not in field_errors:
                        field_errors["non_field_errors"] = [f"Já existe um registro com os campos ({field_list}) informados."]

            if field_errors:
                raise serializers.ValidationError(field_errors)

            return method(self, instance, validated_data)
        return wrapper
    return decorator


def validate_patch_fields(model, unique_fields):
    def decorator(method):
        @wraps(method)
        def wrapper(self, instance, validated_data):
            # Validação de campos nulos ou somente por números
            for field, value in validated_data.items():
                if isinstance(value, str):
                    if not value.strip():
                        raise serializers.ValidationError({field: f"O campo '{field}' é obrigatório."})
                    if not re.search('[a-zA-Z]', value):
                        raise serializers.ValidationError({field: f"O campo '{field}' não pode conter apenas números."})

            # Checar se todos os campos únicos estiverem no PATCH
            if all(field in validated_data for field in unique_fields):
                filter_kwargs = {field: validated_data.get(field, getattr(instance, field)) for field in unique_fields}
                existing = model.objects.filter(**filter_kwargs).exclude(pk=instance.pk)
                if existing.exists():
                    duplicated_values = ', '.join(f"{field}: {filter_kwargs[field]}" for field in unique_fields)
                    raise serializers.ValidationError({
                        'non_field_errors': [f"Já existe um registro com os campos informados: {duplicated_values}."]
                    })

            return method(self, instance, validated_data)
        return wrapper
    return decorator