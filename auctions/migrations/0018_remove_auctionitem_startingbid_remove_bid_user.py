# Generated by Django 4.1.1 on 2022-10-21 23:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0017_auctionitem_minimum'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='auctionitem',
            name='startingBid',
        ),
        migrations.RemoveField(
            model_name='bid',
            name='user',
        ),
    ]
