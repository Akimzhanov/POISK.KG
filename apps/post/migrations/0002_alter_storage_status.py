# Generated by Django 4.1.3 on 2022-11-11 07:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='storage',
            name='status',
            field=models.ForeignKey(choices=[('open', 'Открыто'), ('closed', 'Закрыто')], on_delete=django.db.models.deletion.CASCADE, related_name='posts', to='post.storage'),
        ),
    ]
