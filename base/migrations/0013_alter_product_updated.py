# Generated by Django 4.0.1 on 2022-05-05 09:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0012_alter_product_created_alter_product_updated'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='updated',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
