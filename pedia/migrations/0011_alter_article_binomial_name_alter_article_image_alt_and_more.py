# Generated by Django 4.2.7 on 2023-12-08 09:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pedia', '0010_article_approved'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='binomial_name',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='article',
            name='image_alt',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='article',
            name='map_alt',
            field=models.CharField(max_length=50),
        ),
    ]
