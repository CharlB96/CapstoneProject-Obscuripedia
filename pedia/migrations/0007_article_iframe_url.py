# Generated by Django 4.2.7 on 2023-12-04 11:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pedia', '0006_alter_article_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='iframe_url',
            field=models.URLField(default=''),
        ),
    ]