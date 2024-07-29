from decimal import Decimal

from django.db import models


# Create your models here.

class Service(models.Model):
    SERVICE_TYPES = [
        ('Web Development', 'Web Development'),
        ('Mobile Development', 'Mobile Development'),
        ('Cloud Services', 'Cloud Services'),
        ('Data Analytics', 'Data Analytics'),
        ('Cyber Security', 'Cyber Security'),
        ('Networking', 'Networking'),
        ('IT Support', 'IT Support'),
        ('AI & Machine Learning', 'AI & Machine Learning'),
        ('DevOps', 'DevOps'),
        ('Consulting', 'Consulting'),
    ]

    PAYMENT_TERMS = [
        ('Monthly', 'Monthly'),
        ('Quarterly', 'Quarterly'),
        ('Annually', 'Annually'),
    ]

    SERVICE_PACKAGES = [
        ('Basic', 'Basic'),
        ('Standard', 'Standard'),
        ('Premium', 'Premium'),
    ]


    service_name = models.CharField(max_length=100, choices=SERVICE_TYPES)
    payment_terms = models.CharField(max_length=100, choices=PAYMENT_TERMS)
    service_price = models.DecimalField(max_digits=10, decimal_places=2)
    service_package = models.CharField(max_length=100, choices=SERVICE_PACKAGES)
    service_tax = models.DecimalField(max_digits=10, decimal_places=2)
    service_image = models.ImageField(upload_to='services/')
    active = models.BooleanField(default=True)

    # Calculate service tax as 18% of the service price
    def save(self, *args, **kwargs):
        self.service_tax = self.service_price * Decimal('0.18')
        super(Service, self).save(*args, **kwargs)

    @property
    def total_price(self):
        return self.service_price + self.service_tax
#
# class Address(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     address_line_1 = models.CharField(max_length=255)
#     address_line_2 = models.CharField(max_length=255, blank=True, null=True)
#     city = models.CharField(max_length=100)
#     state = models.CharField(max_length=100)
#     postal_code = models.CharField(max_length=20)
#     country = models.CharField(max_length=100)




