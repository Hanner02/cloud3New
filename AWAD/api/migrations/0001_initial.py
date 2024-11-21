# Generated by Django 4.2.15 on 2024-08-28 14:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ReviewItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('message', models.TextField()),
                ('log_date', models.DateTimeField()),
                ('rating', models.IntegerField(default=0)),
            ],
        ),
    ]
