# Generated by Django 4.2.11 on 2024-05-22 07:48

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('logistics', '0014_remove_invoice_receipient_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='shipment',
            name='additional_charges',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=100, null=True),
        ),
        migrations.AddField(
            model_name='shipment',
            name='additional_kg',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=100, null=True),
        ),
        migrations.AddField(
            model_name='shipment',
            name='description_of_consignment',
            field=models.CharField(default='', max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='shipment',
            name='destination_code',
            field=models.CharField(default='', max_length=40),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='shipment',
            name='dispatched_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='shipment',
            name='insurance_fee',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=100, null=True),
        ),
        migrations.AddField(
            model_name='shipment',
            name='issuing_officer',
            field=models.CharField(default='', max_length=40),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='shipment',
            name='name_of_agent_delivering_consignment',
            field=models.CharField(default='', max_length=40),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='shipment',
            name='name_of_staff_accepting_consignment',
            field=models.CharField(default='', max_length=40),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='shipment',
            name='no_of_pieces',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='shipment',
            name='receipt_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='shipment',
            name='tax_fee',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=100, null=True),
        ),
        migrations.AddField(
            model_name='shipment',
            name='vat_fee',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=100, null=True),
        ),
    ]
