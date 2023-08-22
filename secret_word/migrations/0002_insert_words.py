from django.db import migrations


def insert_words(apps, _schema_editor):
    words = [
        "GARDEN",
        "SPIRIT",
        "EXPERT",
        "CIRCLE",
        "IMPACT",
        "JUNGLE",
        "THEORY",
        "CANDLE",
        "WISDOM",
        "DRAGON",
        "ISLAND",
        "JUNIOR",
        "ROCKET",
        "MEADOW",
        "MARVEL",
        "OUTLET",
        "PLANET",
        "QUIVER",
        "STRONG",
        "TRAVEL",
    ]
    SecretWord = apps.get_model('secret_word', 'SecretWord')
    for word in words:
        SecretWord.objects.create(word=word)


class Migration(migrations.Migration):
    dependencies = [('secret_word', '0001_initial')]
    operations = [migrations.RunPython(insert_words)]
