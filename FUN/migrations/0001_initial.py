# Generated by Django 4.2.1 on 2023-08-25 13:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=50)),
                ('mobile', models.CharField(blank=True, max_length=15, null=True)),
                ('email', models.EmailField(max_length=100, unique=True)),
                ('address', models.TextField(max_length=300)),
                ('image', models.ImageField(default='a.png', upload_to='image/')),
                ('joining_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(auto_now=True)),
                ('city', models.CharField(blank=True, max_length=50, null=True)),
            ],
            options={
                'verbose_name': 'EmployeeData',
            },
        ),
    ]
