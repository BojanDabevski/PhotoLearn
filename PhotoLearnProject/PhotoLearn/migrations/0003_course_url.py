# Generated by Django 4.0.4 on 2022-08-31 13:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PhotoLearn', '0002_articles'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='url',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
    ]