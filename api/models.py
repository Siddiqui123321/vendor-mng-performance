from django.db import models
from django.db.models import F, Count
from datetime import timedelta

class Vendor(models.Model):
    name = models.CharField(max_length=255)
    contact_details = models.TextField()
    address = models.TextField()
    vendor_code = models.CharField(unique=True, max_length=50)
    on_time_delivery_rate = models.FloatField(default=0.0)
    quality_rating_avg = models.FloatField(default=0.0)
    average_response_time = models.FloatField(default=0.0)
    fulfillment_rate = models.FloatField(default=0.0)



class PurchaseOrder(models.Model):
    po_number = models.CharField(unique=True, max_length=50)
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE)
    order_date = models.DateTimeField()
    delivery_date = models.DateTimeField()
    items = models.JSONField()
    quantity = models.IntegerField()
    status = models.CharField(max_length=50)
    quality_rating = models.FloatField(null=True, blank=True)
    issue_date = models.DateTimeField()
    acknowledgment_date = models.DateTimeField(null=True, blank=True)


# On-Time Delivery Rate:
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if self.status == 'completed':
            completed_orders = PurchaseOrder.objects.filter(
                vendor=self.vendor, status='completed'
            )
            on_time_orders = completed_orders.filter(
                delivery_date__lte=F('acknowledgment_date')
            )
            on_time_delivery_rate = (
                on_time_orders.count() / completed_orders.count()
            ) * 100 if completed_orders.count() > 0 else 0.0
            self.vendor.on_time_delivery_rate = on_time_delivery_rate
            self.vendor.save()

# Quality Rating Average:
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if self.quality_rating is not None and self.status == 'completed':
            completed_orders = PurchaseOrder.objects.filter(
                vendor=self.vendor, status='completed'
            )
            quality_ratings = completed_orders.exclude(quality_rating=None).values_list(
                'quality_rating', flat=True
            )
            quality_rating_avg = (
                sum(quality_ratings) / len(quality_ratings)
            ) if len(quality_ratings) > 0 else 0.0
            self.vendor.quality_rating_avg = quality_rating_avg
            self.vendor.save()

# Average Response Time:
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if self.acknowledgment_date is not None:
            response_times = PurchaseOrder.objects.filter(
                vendor=self.vendor, acknowledgment_date__isnull=False
            ).values_list('acknowledgment_date', 'issue_date')

            average_response_time = (
                sum((ack_date - issue_date).total_seconds() for ack_date, issue_date in response_times)
                / len(response_times)
            ) if len(response_times) > 0 else 0.0

            self.vendor.average_response_time = average_response_time
            self.vendor.save()

# Fulfillment Rate:
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        all_orders = PurchaseOrder.objects.filter(vendor=self.vendor)
        successful_orders = all_orders.filter(status='completed', quality_rating__isnull=False)
        fulfillment_rate = (
            (successful_orders.count() / all_orders.count()) * 100
        ) if all_orders.count() > 0 else 0.0

        self.vendor.fulfillment_rate = fulfillment_rate
        self.vendor.save()


class HistoricalPerformance(models.Model):
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE)
    date = models.DateTimeField()
    on_time_delivery_rate = models.FloatField()
    quality_rating_avg = models.FloatField()
    average_response_time = models.FloatField()
    fulfillment_rate = models.FloatField()

