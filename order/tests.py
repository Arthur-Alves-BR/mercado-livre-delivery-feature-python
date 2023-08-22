from django.contrib.auth.models import User

from rest_framework import status
from rest_framework.test import APITestCase, APIClient

from requests import Response

from order.models import Order
from secret_word.models import SecretWord


class OrderTestCase(APITestCase):
    def setUp(self):
        self._url = '/orders'
        self._create_test_data()
        self._api_client = APIClient()

    def test_close_order_with_wrong_word(self):
        response = self._try_to_close_order(self._order.id, 'ABCDEF')
        self._order.refresh_from_db()

        self.assertFalse(self._order.delivered)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_close_order_with_right_word(self):
        response = self._try_to_close_order(self._order.id, self._secret_word.word)
        self._order.refresh_from_db()

        self.assertTrue(self._order.delivered)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_already_closed_order(self):
        response = self._try_to_close_order(self._closed_order.id, self._secret_word.word)
        self.assertEqual(response.status_code, status.HTTP_409_CONFLICT)

    def _try_to_close_order(self, order_id: int, word: str) -> Response:
        return self._api_client.post(f'{self._url}/{order_id}/close/', {'word': word})

    def _create_test_data(self):
        self._user = User.objects.create()
        self._secret_word = SecretWord.objects.first()

        self._order = Order.objects.create(
            secret_word=self._secret_word,
            user=self._user,
        )

        self._closed_order = Order.objects.create(
            secret_word=self._secret_word,
            user=self._user,
            delivered=True,
        )
