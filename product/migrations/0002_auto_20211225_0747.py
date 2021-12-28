# Generated by Django 3.0.2 on 2021-12-25 07:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='description',
            field=models.TextField(blank=True, default='', max_length=3000, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='product_expires',
            field=models.DateField(),
        ),
    ]
