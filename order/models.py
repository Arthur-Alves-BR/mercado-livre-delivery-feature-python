from django.db import models
from django.contrib.auth.models import User

from secret_word.models import SecretWord


class Order(models.Model):
    id = models.AutoField(primary_key=True)
    delivered = models.BooleanField(default=False)
    created_at = models.DateTimeField(blank=False, null=False, auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING, blank=False, null=False)
    secret_word = models.ForeignKey(SecretWord, on_delete=models.PROTECT, blank=False, null=False)

    class Meta:
        db_table = 'orders'

    def secret_word_match(self, word: str) -> bool:
        return self.secret_word.word == word
