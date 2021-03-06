# Generated by Django 3.0.8 on 2020-07-02 15:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_id', models.IntegerField()),
                ('company_name', models.CharField(max_length=128)),
                ('url', models.URLField()),
                ('address', models.CharField(max_length=128)),
                ('industry', models.CharField(max_length=64)),
            ],
        ),
    ]
