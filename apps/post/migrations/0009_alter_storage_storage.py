# Generated by Django 4.1.3 on 2022-11-11 08:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0008_alter_storage_storage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='storage',
            name='storage',
            field=models.ForeignKey(blank=True, choices=[('lost', 'Потерял'), ('find', 'Нашел')], null=True, on_delete=django.db.models.deletion.CASCADE, related_name='posts', to='post.storage'),
        ),
    ]
