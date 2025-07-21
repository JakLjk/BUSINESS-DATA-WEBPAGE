# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class BusinessDataApiLogs(models.Model):
    logger_session_id = models.CharField(blank=True, null=True)
    timestamp = models.DateTimeField(blank=True, null=True)
    level = models.CharField(blank=True, null=True)
    logger_name = models.CharField(blank=True, null=True)
    message = models.CharField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'business_data_api_logs'


class CompanyInfo(models.Model):
    record_created_at = models.DateTimeField(blank=True, null=True)
    is_current = models.BooleanField(blank=True, null=True)
    full_name = models.CharField(max_length=250)
    legal_form = models.CharField(max_length=100)
    krs_number = models.CharField(max_length=14)
    nip_number = models.CharField(max_length=10)
    regon_number = models.CharField(max_length=14)
    country = models.CharField(max_length=100, blank=True, null=True)
    voivodeship = models.CharField(max_length=100, blank=True, null=True)
    municipality = models.CharField(max_length=100, blank=True, null=True)
    county = models.CharField(max_length=100, blank=True, null=True)
    city = models.CharField(max_length=100, blank=True, null=True)
    postal_number = models.CharField(max_length=6, blank=True, null=True)
    street = models.CharField(max_length=100, blank=True, null=True)
    house_number = models.CharField(max_length=20, blank=True, null=True)
    email = models.CharField(max_length=320, blank=True, null=True)
    webpage = models.CharField(max_length=2083, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'company_info'


class CompanyInfoDetails(models.Model):
    is_current = models.BooleanField(blank=True, null=True)
    record_created_at = models.DateTimeField(blank=True, null=True)
    registered_at_krs_system_date = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'company_info_details'


class KrsDfDocuments(models.Model):
    hash_id = models.CharField(primary_key=True)
    krs_number = models.CharField(blank=True, null=True)
    document_internal_id = models.CharField(blank=True, null=True)
    document_type = models.CharField(blank=True, null=True)
    document_name = models.CharField(blank=True, null=True)
    document_date_from = models.CharField(blank=True, null=True)
    document_date_to = models.CharField(blank=True, null=True)
    document_status = models.CharField(blank=True, null=True)
    document_content_save_name = models.CharField(blank=True, null=True)
    document_content_file_extension = models.CharField(blank=True, null=True)
    document_content = models.BinaryField(blank=True, null=True)
    record_created_at = models.DateTimeField(blank=True, null=True)
    record_updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'krs_df_documents'


class RawKrsApiFullExtract(models.Model):
    record_created_at = models.DateTimeField(blank=True, null=True)
    is_current = models.BooleanField(blank=True, null=True)
    krs_number = models.CharField(max_length=10)
    raw_data = models.JSONField()

    class Meta:
        managed = False
        db_table = 'raw_krs_api_full_extract'
