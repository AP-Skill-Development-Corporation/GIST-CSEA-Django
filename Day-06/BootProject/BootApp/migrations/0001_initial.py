# Generated by Django 3.0 on 2023-03-03 07:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('usname', models.CharField(max_length=120)),
                ('pwd', models.CharField(max_length=120)),
                ('email', models.EmailField(max_length=200)),
            ],
        ),
    ]
