# Generated by Django 4.1.3 on 2022-11-11 12:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0011_alter_storage_storage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='storage',
            name='storage',
            field=models.CharField(choices=[('lost', 'Потерял'), ('find', 'Нашел')], max_length=20),
        ),
    ]