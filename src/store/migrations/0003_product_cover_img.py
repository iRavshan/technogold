# Generated by Django 4.1.8 on 2023-05-02 14:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_productimage'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='cover_img',
            field=models.FileField(default=None, null=True, upload_to='products/'),
        ),
    ]