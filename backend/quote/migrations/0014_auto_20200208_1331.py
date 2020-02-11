# Generated by Django 2.2.9 on 2020-02-08 13:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quote', '0013_quoteprocess_start_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='quoteprocess',
            name='deposit_amount',
        ),
        migrations.AddField(
            model_name='quoteprocess',
            name='quote_amount',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=7, null=True, verbose_name='Quote Amount'),
        ),
    ]