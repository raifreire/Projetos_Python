<<<<<<< HEAD
# Generated by Django 4.2 on 2023-05-02 01:21
=======
# Generated by Django 4.2 on 2023-05-05 15:09
>>>>>>> 2f5fab690d09db417c506f35e833c341c0e6db77

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('galeria', '0003_fotografia_publicada'),
    ]

    operations = [
        migrations.AddField(
            model_name='fotografia',
            name='data_fotografia',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
    ]
