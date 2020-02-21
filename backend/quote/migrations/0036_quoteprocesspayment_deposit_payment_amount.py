# Generated by Django 2.2.10 on 2020-02-21 10:15

from django.db import migrations, models
from django.db.models import F, Subquery, OuterRef


def populate_deposit_payment_amount(apps, schema_editor):
  QuoteProcessPayment = apps.get_model('quote', 'QuoteProcessPayment')
  QuoteProcessPayment.objects.all().annotate(
      quote_deposit=Subquery(QuoteProcessPayment.objects.filter(
          pk=OuterRef('pk')).values('quote_process__deposit')[:1])
  ).update(
      deposit_payment_amount=models.F(
          'official_hereford_quote') * models.F('quote_deposit') / 100
  )

class Migration(migrations.Migration):

    dependencies = [
        ('quote', '0035_auto_20200220_1517'),
    ]

    operations = [
        migrations.AddField(
            model_name='quoteprocesspayment',
            name='deposit_payment_amount',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=7, verbose_name='Deposit Payment Amount'),
            preserve_default=False,
        ),
        migrations.RunPython(populate_deposit_payment_amount, migrations.RunPython.noop)
    ]