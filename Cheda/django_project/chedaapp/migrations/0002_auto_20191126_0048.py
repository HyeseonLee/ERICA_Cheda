# Generated by Django 2.2.7 on 2019-11-25 15:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chedaapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='item',
            old_name='to_finn_date',
            new_name='to_fin_date',
        ),
    ]
