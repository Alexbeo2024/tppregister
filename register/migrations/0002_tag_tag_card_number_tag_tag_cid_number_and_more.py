# Generated by Django 4.2.10 on 2024-03-04 21:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("register", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="tag",
            name="tag_card_number",
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name="TAGCardNumber"),
        ),
        migrations.AddField(
            model_name="tag",
            name="tag_cid_number",
            field=models.CharField(blank=True, max_length=200, null=True, unique=True, verbose_name="TAGCIDCode"),
        ),
        migrations.AddField(
            model_name="tag",
            name="tag_contract_number",
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name="TAGContractNumber"),
        ),
        migrations.AddField(
            model_name="tag",
            name="tag_service_name",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="register.service",
                verbose_name="ServiceName",
            ),
        ),
    ]
