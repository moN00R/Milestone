from django.db.models.signals import post_save, post_delete, pre_delete
from django.dispatch import receiver
from courses.models import Subscription


@receiver(post_save, sender=Subscription, weak=False)
def create_subscription(sender, instance, **kwargs):
    course = instance.course
    course.number_of_student += 1
    print(course)
    course.save()


@receiver(post_delete, sender=Subscription, weak=False)
def delete_subscription(sender, instance,  **kwargs):
    course = instance.course
    course.number_of_student -= 1
    course.save()  
