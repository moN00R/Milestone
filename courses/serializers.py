from rest_framework.exceptions import ValidationError, AuthenticationFailed
from rest_framework import serializers
from marks.models import StudentMark
from accounts.serializers import CreateUserSerializer
from .models import *


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ['id', "name", "description",
                  "days_to_start", "days", "hours",]


class SubscriptionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Subscription
        fields = ['id', 'course_id', 'course', 'user']
        extra_kwargs = {
            'user': {'read_only': True}
        }

    course_id = serializers.IntegerField(write_only=True)
    course = CourseSerializer(read_only=True,)
    user = CreateUserSerializer(read_only=True)

    def validate(self, attrs):

        course = Course.objects.get(id=attrs['course_id'], active=True)
        self.course = course

        user = self.context['request'].user
        if course.open_to_booking == False:
            raise ValidationError('you cant register in this course')

        if course.number_of_student == course.limit_booking:
            course.open_to_booking = False
            course.save()
            raise ValidationError('you cant subsecript now.')

        if course.number_of_student > course.limit_booking:
            raise ValidationError('you cant subsecript now.')

        if Subscription.objects.filter(user=user, course=course).exists():
            raise ValidationError('already exist')

        return attrs

    def create(self, validated_data):
        course = self.course
        user = self.context['request'].user
        subscription = Subscription.objects.create(
            user=user, course_id=course.id)
        return subscription
