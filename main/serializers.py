from rest_framework import serializers
from main.models import  Company, Types


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = '__all__'


# class CompanySerializer(serializers.Serializer):
#     name = serializers.CharField(max_length=255)
#     created = serializers.DateTimeField(read_only=True)
#     not_paid = serializers.IntegerField(default=0)
#     has_fine = serializers.BooleanField(default=False)
#     paid_before = serializers.BooleanField(default=False)
#     for_militiary = serializers.BooleanField(default=False)
#
#     def create(self, validated_data):
#         return Company.objects.create(**validated_data)
#
#     def update(self, instance, validated_data):
#         instance.name = validated_data.get('name', instance.name)
#         instance.not_paid = validated_data.get('not_paid', instance.not_paid)
#         instance.has_fine = validated_data.get('has_fine', instance.has_fine)
#         instance.paid_before = validated_data.get('paid_before', instance.paid_before)
#         instance.for_militiary = validated_data.get('for_militiary', instance.for_militiary)
#         instance.save()
#         return instance
