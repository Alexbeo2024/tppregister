from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

CURRENCY_CHOICES = [
    ("EUR", "EUR"),
    ("DIN", "DIN"),
]


# Create your models here.
class FuelCardIssuer(models.Model):
    fci_name = models.CharField(
        _("FCIName"),
        max_length=255,
        unique=True,
    )
    fci_full_name = models.CharField(
        _("FCIFullName"),
        max_length=255,
        unique=True,
        blank=True,
    )
    fci_address = models.CharField(_("FCIAddress"), max_length=255, blank=True)
    fci_city = models.CharField(_("FCICity"), max_length=255, blank=True)
    fci_country = models.CharField(_("FCICountry"), max_length=255, blank=True)
    fci_email = models.EmailField(_("FCIEmail"), blank=True)
    fci_reg_number = models.CharField(_("FCIRegNumber"), max_length=30, blank=True)
    fci_vat_number = models.CharField(_("FCIVatNumber"), max_length=30, blank=True)
    fci_resident_company = models.BooleanField(_("FCIResident"), default=False)
    fci_payment_currency = models.CharField(_("FCICurrency"), choices=CURRENCY_CHOICES, default="DIN", max_length=3)
    fci_date_create = models.DateField(_("FCIDateCreate"), auto_now_add=True)

    def __str__(self):
        return self.fci_name

    @property
    def activated_tags_count(self):
        return self.tag_set.filter(tag_fci_name__tag__isnull=False).count()


class Company(models.Model):
    company_fci_name = models.ForeignKey(
        FuelCardIssuer, on_delete=models.CASCADE, verbose_name=_("FCIName"), blank=True, null=True
    )
    company_name = models.CharField(
        _("CompanyName"),
        max_length=255,
        unique=True,
    )
    company_full_name = models.CharField(
        _("CompanyFullName"),
        max_length=255,
        unique=True,
        blank=True,
    )
    company_address = models.CharField(_("CompanyAddress"), max_length=255, blank=True)
    company_city = models.CharField(_("CompanyCity"), max_length=255, blank=True)
    company_country = models.CharField(_("CompanyCountry"), max_length=255, blank=True)
    company_email = models.EmailField(_("CompanyEmail"), blank=True)
    company_reg_number = models.CharField(_("CompanyRegNumber"), max_length=30, blank=True)
    company_vat_number = models.CharField(_("CompanyVatNumber"), max_length=30, blank=True)
    company_resident_company = models.BooleanField(_("CompanyResident"), default=False)
    company_date_create = models.DateField(_("CompanyDateCreate"), auto_now_add=True)

    def __str__(self):
        return self.company_name


class Service(models.Model):
    service_fci_name = models.ForeignKey(
        FuelCardIssuer, on_delete=models.CASCADE, verbose_name=_("FCIName"), blank=True, null=True
    )
    type_of_service = models.CharField(
        _("TypeOfService"),
        max_length=255,
        unique=True,
    )
    price_of_service = models.IntegerField(_("PriceOfService"))

    def __str__(self):
        return self.type_of_service


class TAG(models.Model):
    tag_fci_name = models.ForeignKey(
        FuelCardIssuer,
        on_delete=models.CASCADE,
        verbose_name=_("FCIName"),
        blank=True,
        null=True,
    )

    tag_company_name = models.ForeignKey(
        Company,
        on_delete=models.CASCADE,
        verbose_name=_("CompanyName"),
        blank=True,
        null=True,
    )
    tag_service_name = models.ForeignKey(
        Service,
        on_delete=models.CASCADE,
        verbose_name=_("ServiceName"),
        blank=True,
        null=True,
    )
    tag_barcode_number = models.CharField(_("TAGBarCode"), max_length=200, blank=True, null=True, unique=True)
    tag_cid_number = models.CharField(_("TAGCIDCode"), max_length=200, blank=True, null=True, unique=True)
    tag_contract_number = models.CharField(_("TAGContractNumber"), max_length=200, blank=True, null=True)
    tag_card_number = models.CharField(_("TAGCardNumber"), max_length=200, blank=True, null=True)
    tag_car_number = models.CharField(_("TAGCarNumber"), max_length=200, blank=True, null=True)
    tag_car_category = models.CharField(_("TAGCarCategory"), max_length=200, blank=True, null=True)
    tag_macedonia = models.BooleanField(_('Macedonia'), default=False)
    tag_croatia =  models.BooleanField(_('Croatia'), default=False)
    tag_montenegro = models.BooleanField(_('Montenegro'), default=False)
    tag_greece = models.BooleanField(_('Greece'), default=False)
    tag_bih = models.BooleanField(_('BiH'), default=False)
    tag_registration = models.DateTimeField(_('TagRegistrationTime'), default=timezone.now)
    tag_blocked = models.BooleanField(_('TAGBlocked'), default=False)
    tag_last_blocked = models.DateTimeField(_('LastBlocked'), default=timezone.now)
    tag_last_activate = models.DateTimeField(_('LastActivate'), default=timezone.now)
