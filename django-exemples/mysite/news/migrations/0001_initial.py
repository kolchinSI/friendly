# Generated by Django 2.1.7 on 2019-02-15 19:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Articles',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titles', models.CharField(max_length=120)),
                ('post', models.TextField()),
                ('date', models.DateTimeField()),
            ],
        ),
    ]