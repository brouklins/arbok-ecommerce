# Generated by Django 4.1.1 on 2022-09-14 21:33

from django.db import migrations, models
import djongo.models.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('_id', djongo.models.fields.ObjectIdField(auto_created=True, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('category', models.CharField(max_length=255)),
                ('brand', models.CharField(max_length=255)),
                ('description', models.CharField(max_length=255)),
                ('stock', models.IntegerField()),
                ('active', models.BooleanField()),
                ('rating', models.IntegerField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=7)),
                ('create_at', models.DateField(auto_now_add=True)),
            ],
        ),
    ]
