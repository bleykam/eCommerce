# Generated by Django 4.1.1 on 2022-10-29 17:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0022_remove_user_notes_comment_user'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Watch',
        ),
        migrations.AddField(
            model_name='watchlist',
            name='watched',
            field=models.BooleanField(default=False),
        ),
    ]
