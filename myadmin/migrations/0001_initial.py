# Generated by Django 3.0.5 on 2022-03-07 14:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='MyAdmin',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reg_id', models.CharField(editable=False, max_length=40)),
                ('total_revenue', models.FloatField(default=0.0)),
                ('is_active', models.BooleanField(default=True)),
                ('points', models.FloatField(default=0.0)),
                ('is_subscribed', models.BooleanField(default=False)),
                ('subscription_expiry', models.DateTimeField()),
                ('free_plan_expired', models.BooleanField(default=False)),
                ('secret_pin', models.CharField(default='0000', max_length=4)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='user_admin', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='WalletAddress',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('coin_name', models.CharField(help_text='full name of coin,e.g Bitcoin', max_length=30)),
                ('coin_code', models.CharField(help_text='coin code w.g BTC', max_length=15)),
                ('address', models.CharField(help_text='enter your own wallet address for this,ensure its correct', max_length=200)),
                ('admin', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='wallet_address', to='myadmin.MyAdmin')),
            ],
        ),
        migrations.CreateModel(
            name='Subscription',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('transaction_reference', models.TextField()),
                ('is_approved', models.BooleanField(default=False)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('date_approved', models.DateTimeField(blank=True, null=True)),
                ('admin', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myadmin.MyAdmin')),
            ],
        ),
        migrations.CreateModel(
            name='Settings',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reg_email_verify', models.BooleanField(default=False, help_text='enable email verification on registration')),
                ('enable_newsletters', models.BooleanField(default=False)),
                ('enable_transaction_emails', models.BooleanField(default=False)),
                ('enable_referral_bonus', models.BooleanField(default=False)),
                ('enable_watsapp_chat', models.BooleanField(default=False)),
                ('enable_social_links', models.BooleanField(default=False)),
                ('enable_registration_emails', models.BooleanField(default=False, help_text='send emails to users upon registration')),
                ('admin', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='settings', to='myadmin.MyAdmin')),
            ],
        ),
    ]
