# Generated by Django 4.2.7 on 2024-01-11 01:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_rename_store_custo_last_na_e6a359_idx_store_custo_last_na_2e448d_idx_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='slug',
            field=models.SlugField(default=1),
            preserve_default=False,
        ),
    ]
