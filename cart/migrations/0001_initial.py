# Generated by Django 4.1 on 2022-08-24 05:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('descriptions', models.CharField(max_length=200)),
                ('price', models.FloatField(null=True)),
                ('rating', models.DecimalField(decimal_places=0, max_digits=5)),
            ],
        ),
    ]
