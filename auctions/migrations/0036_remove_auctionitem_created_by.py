# Generated by Django 4.1.1 on 2022-11-10 18:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0035_auctionitem_created_by'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='auctionitem',
            name='created_by',
        ),
    ]
