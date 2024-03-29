# Generated by Django 4.2.10 on 2024-03-17 14:31

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ("register", "0002_tag_tag_card_number_tag_tag_cid_number_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="company",
            name="company_payment_currency",
        ),
        migrations.AddField(
            model_name="tag",
            name="tag_bih",
            field=models.BooleanField(default=False, verbose_name="BiH"),
        ),
        migrations.AddField(
            model_name="tag",
            name="tag_blocked",
            field=models.BooleanField(default=False, verbose_name="TAGBlocked"),
        ),
        migrations.AddField(
            model_name="tag",
            name="tag_car_category",
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name="TAGCarCategory"),
        ),
        migrations.AddField(
            model_name="tag",
            name="tag_car_number",
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name="TAGCarNumber"),
        ),
        migrations.AddField(
            model_name="tag",
            name="tag_croatia",
            field=models.BooleanField(default=False, verbose_name="Croatia"),
        ),
        migrations.AddField(
            model_name="tag",
            name="tag_greece",
            field=models.BooleanField(default=False, verbose_name="Greece"),
        ),
        migrations.AddField(
            model_name="tag",
            name="tag_last_activate",
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name="LastActivate"),
        ),
        migrations.AddField(
            model_name="tag",
            name="tag_last_blocked",
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name="LastBlocked"),
        ),
        migrations.AddField(
            model_name="tag",
            name="tag_macedonia",
            field=models.BooleanField(default=False, verbose_name="Macedonia"),
        ),
        migrations.AddField(
            model_name="tag",
            name="tag_montenegro",
            field=models.BooleanField(default=False, verbose_name="Montenegro"),
        ),
        migrations.AddField(
            model_name="tag",
            name="tag_registration",
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name="TagRegistrationTime"),
        ),
    ]
