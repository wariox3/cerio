# Generated by Django 5.0.6 on 2024-06-07 18:16

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('general', '0002_solicitud'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name='solicitud',
            name='usuario_asignado',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='solicitudes_usuario_asignado_rel', to=settings.AUTH_USER_MODEL),
        ),
    ]
