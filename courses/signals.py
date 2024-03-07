from django.db.models.signals import post_save, post_delete, pre_delete
from django.dispatch import receiver
from .models import Subscription, Course


@receiver(post_save, sender=Subscription)
def create_subscription(sender, instance, **kwargs):
    course = instance.course
    course.number_of_student = course.number_of_student + 1
    course.save()


@receiver(post_delete, sender=Subscription)
def delete_subscription(sender, instance,  **kwargs):
    course = instance.course
    course.number_of_student = course.number_of_student - 1
    course.save()



