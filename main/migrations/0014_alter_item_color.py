# Generated by Django 4.2.5 on 2023-11-09 12:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0013_alter_item_color'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='color',
            field=models.CharField(choices=[('Blue', 'Blue'), ('Red', 'Red'), ('Green', 'Green'), ('Yellow', 'Yellow'), ('Purple', 'Purple'), ('Black', 'Black'), ('White', 'White')], max_length=11),
        ),
    ]
