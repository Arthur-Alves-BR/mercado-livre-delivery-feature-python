from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.exceptions import MethodNotAllowed

from order.models import Order
from order.serializers import OrderSerializer, CloseOrderSerializer


class OrderViewSet(viewsets.ModelViewSet):
    serializer_class = OrderSerializer
    queryset = Order.objects.all()

    def destroy(self, request, *_args, **_kwargs):
        raise MethodNotAllowed('DELETE')

    @action(methods=['POST'], detail=True, url_path='close')
    def close_order(self, request, *_args, **_kwargs):
        serializer = CloseOrderSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        order: Order = self.get_object()

        if order.delivered:
            return Response(None, status=status.HTTP_409_CONFLICT)

        if not order.secret_word_match(serializer.data.get('word', '')):
            return Response(None, status=status.HTTP_401_UNAUTHORIZED)

        order.delivered = True
        order.save()

        return Response(None, status=status.HTTP_204_NO_CONTENT)
