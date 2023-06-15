# Generated by Django 4.2.2 on 2023-06-15 05:15

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_pizza_description'),
    ]

    operations = [
        migrations.CreateModel(
            name='Offers',
            fields=[
                ('uid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateField(auto_now_add=True)),
                ('updated_at', models.DateField(auto_now_add=True)),
                ('offer_title', models.CharField(max_length=100)),
                ('offer_description', models.CharField(max_length=500)),
                ('offer_tc', models.CharField(max_length=500)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]