# Generated by Django 4.1.6 on 2023-02-05 15:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_post_podt_data'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='podt_data',
            new_name='post_date',
        ),
    ]
