# Generated by Django 4.2.5 on 2023-09-12 11:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('item', '0002_alter_category_options_item'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='name',
            field=models.CharField(default='category.name', max_length=255),
        ),
    ]