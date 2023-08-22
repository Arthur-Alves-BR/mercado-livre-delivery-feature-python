from django.db import models


class SecretWord(models.Model):
    id = models.AutoField(primary_key=True)
    word = models.CharField(max_length=6)

    class Meta:
        db_table = 'secret_words'
