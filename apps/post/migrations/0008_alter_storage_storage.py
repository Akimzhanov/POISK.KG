# Generated by Django 4.1.3 on 2022-11-11 08:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0007_alter_storage_storage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='storage',
            name='storage',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='post_post', to='post.storage'),
        ),
    ]