# Generated by Django 4.1.1 on 2022-10-09 19:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0005_auctionitem_bids_auctionitem_comments_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='WatchList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('watch', models.URLField(max_length=100)),
            ],
        ),
    ]
