# Generated by Django 4.2.11 on 2024-05-20 09:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('logistics', '0013_rename_invoice_id_invoice_invoice_number'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='invoice',
            name='receipient_email',
        ),
    ]
