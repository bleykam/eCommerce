# Generated by Django 4.1.1 on 2022-10-08 12:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0002_bid_comment_listing'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='image',
            field=models.URLField(blank=True),
        ),
        migrations.AlterField(
            model_name='listing',
            name='startingBid',
            field=models.IntegerField(default=0),
        ),
    ]