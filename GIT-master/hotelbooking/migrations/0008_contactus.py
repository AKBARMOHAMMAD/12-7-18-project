# Generated by Django 2.1.3 on 2018-12-04 08:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotelbooking', '0007_userregister'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactUs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('Email_id', models.EmailField(max_length=254)),
                ('phone_no', models.IntegerField()),
                ('message', models.CharField(max_length=220)),
            ],
        ),
    ]