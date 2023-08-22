from rest_framework import serializers

from order.models import Order
from secret_word.models import SecretWord


class OrderSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        validated_data['secret_word'] = SecretWord.objects.order_by('?').first()
        # Here you send an email with the secret to the customer
        # send_email_to_customer(...)
        return super().create(validated_data)

    class Meta:
        model = Order
        extra_kwargs = {
            'delivered': {'read_only': True},
        }
        exclude = ['secret_word']


class CloseOrderSerializer(serializers.Serializer):
    word = serializers.CharField(required=True)
