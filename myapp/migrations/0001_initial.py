# Generated by Django 4.2.6 on 2023-10-11 05:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CustomerImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer_name', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to='customer_images/')),
                ('upload_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
