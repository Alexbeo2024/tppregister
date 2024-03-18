from django.contrib import admin
from .models import FuelCardIssuer, Company


class FuelCardIssuerAdmin(admin.ModelAdmin):
    list_display = (
        "fci_name",
        "fci_full_name",
        "fci_address",
        "fci_city",
        "fci_country",
        "fci_email",
        "fci_reg_number",
        "fci_vat_number",
        "fci_resident_company",
        "fci_payment_currency",
        "fci_date_create",
    )
    list_editable = ("fci_payment_currency", "fci_resident_company",)
    search_fields = (
        "fci_name",
        "fci_full_name",
        "fci_reg_number",
        "fci_vat_number",
    )
    ordering = ("fci_name",)

class CompanyAdmin(admin.ModelAdmin):
    list_display = ('company_name', 'company_full_name', 'company_email')
    search_fields = ('company_name', 'company_full_name', 'company_email')

admin.site.register(FuelCardIssuer, FuelCardIssuerAdmin)
admin.site.register(Company, CompanyAdmin)
