# Generated by Django 4.2.7 on 2023-12-01 11:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pedia', '0003_article_image_alt'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='binomial_name',
            field=models.CharField(default='(Genus) (Species)', max_length=50),
        ),
    ]
