# Generated by Django 3.0.8 on 2020-08-25 14:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Tutorial', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.DeleteModel(
            name='Credentials',
        ),
    ]
