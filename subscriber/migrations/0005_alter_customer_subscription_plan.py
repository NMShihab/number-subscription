# Generated by Django 3.2.9 on 2021-11-10 19:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('subscriber', '0004_alter_customer_subscription_plan'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='subscription_plan',
            field=models.ForeignKey(max_length=100, null=True, on_delete=django.db.models.deletion.SET_NULL, to='subscriber.subscriptionplan'),
        ),
    ]