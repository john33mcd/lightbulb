# Generated by Django 3.2.19 on 2023-05-11 19:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_alter_review_rating'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='title',
            field=models.CharField(default='Please give your review a title', max_length=200, unique=True),
        ),
    ]
