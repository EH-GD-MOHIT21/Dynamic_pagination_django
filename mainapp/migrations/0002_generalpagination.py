# Generated by Django 3.2.2 on 2021-05-11 10:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='generalpagination',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('extra', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.paginationdata')),
            ],
        ),
    ]