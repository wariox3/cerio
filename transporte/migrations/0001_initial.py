# Generated by Django 5.0.6 on 2024-06-07 17:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Carroceria',
            fields=[
                ('id', models.BigIntegerField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'tte_carroceria',
            },
        ),
    ]
