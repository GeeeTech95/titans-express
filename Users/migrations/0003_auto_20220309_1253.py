# Generated by Django 3.0.5 on 2022-03-09 07:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Users', '0002_auto_20220308_1521'),
    ]

    operations = [
        migrations.AddField(
            model_name='settings',
            name='password_on_withdrawal',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='settings',
            name='email_on_transaction',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='_wallet_address',
            field=models.CharField(help_text='BEP20 address', max_length=40, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='_wallet_name',
            field=models.CharField(choices=[('BTC', 'BTC'), ('ETH', 'ETH'), ('USDT', 'USDT'), ('LTC', 'LTC')], max_length=10, null=True),
        ),
        migrations.CreateModel(
            name='Security',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('otp', models.PositiveIntegerField(blank=True, null=True)),
                ('otp_expiry', models.DateTimeField(blank=True, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='security', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
