# Generated by Django 2.2.9 on 2020-02-27 15:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('quote', '0038_merge_20200226_1046'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quoteprocessdocuments',
            name='hsr',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='hellosign_app.HelloSignSignatureRequest', verbose_name='HelloSign Request'),
        ),
    ]
