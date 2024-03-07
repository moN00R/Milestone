from rest_framework import serializers
from courses.models import Subscription
from courses.serializers import SubscriptionSerializer
from .models import StudentMark


class StudentMarksSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentMark
        fields = '__all__'

        extra_kwargs = {

            'user': {'read_only': True},
        }

    subscription_course = SubscriptionSerializer()

    def get_subscription_course(self):
        user = self.context['request'].user
        return Subscription.objects.filter(user=user)
    # def validate(self, attrs):
    #     user = self.context['request'].user
    #     student_course = Subscription.objects.filter(user=user)
    #     return attrs

    # def to_representation(self, instance):
    #     return super().to_representation(instance)
