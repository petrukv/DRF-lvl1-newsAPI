# Generated by Django 4.2.5 on 2024-02-12 21:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0002_journalist_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='author',
            field=models.CharField(max_length=50),
        ),
        migrations.DeleteModel(
            name='Journalist',
        ),
    ]
