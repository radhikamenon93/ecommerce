# Generated by Django 4.2.6 on 2024-01-15 11:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('description', models.TextField(max_length=200)),
                ('image', models.ImageField(null=True, upload_to='images')),
                ('status', models.BooleanField(default=False)),
            ],
        ),
    ]
