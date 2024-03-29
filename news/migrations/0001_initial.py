# Generated by Django 4.2.5 on 2024-02-12 17:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(max_length=50)),
                ('title', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=150)),
                ('body', models.TextField()),
                ('location', models.CharField(max_length=50)),
                ('publication', models.DateField()),
                ('active', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
