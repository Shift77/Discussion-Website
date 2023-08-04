# Generated by Django 4.2 on 2023-08-04 14:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('discussion_app', '0006_alter_message_options'),
        ('core_app', '0005_alter_userprofile_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='saved_posts',
            field=models.ManyToManyField(blank=True, to='discussion_app.post'),
        ),
    ]