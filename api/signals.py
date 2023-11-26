from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import PurchaseOrder

@receiver(post_save, sender=PurchaseOrder)
def purchase_order_saved(sender, instance, created, **kwargs):
    # Logic to execute when a PurchaseOrder is saved
    # This could include triggering calculations or updates
    if instance.status == 'completed':
        instance.calculate_on_time_delivery_rate()
        instance.calculate_quality_rating_avg()
        instance.calculate_fulfillment_rate()
        instance.create_historical_performance()

    if instance.status == 'cancelled':
        instance.calculate_fulfillment_rate()

    if instance.acknowledgment_date is not None:
        instance.calculate_average_response_time()
