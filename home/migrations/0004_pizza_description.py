# Generated by Django 4.2.2 on 2023-06-13 13:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_card_details'),
    ]

    operations = [
        migrations.AddField(
            model_name='pizza',
            name='description',
            field=models.CharField(default='', max_length=500),
            preserve_default=False,
        ),
    ]
