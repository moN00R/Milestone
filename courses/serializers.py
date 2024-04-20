from rest_framework import serializers
from courses.models import Course, CourseType, Subscription
# from account_user.serializers import UserinfoSerializer

class CourseTypeserializer(serializers.ModelSerializer):
    class Meta:
        model = CourseType
        fields = (
            'id', 
            'name'     
        )

class CoursesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = (
            'id',
            'name', 
            'description', 
            'image', 
            'days', 
            'hours', 
            'category',
            'active',
        )
    
    category = CourseTypeserializer()

class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscription
        fields = (
            'id',
            'phonenumber',
            'course',
        )
        
    def validate(self, attrs):
        course = attrs['course']
        phonenumber = attrs['phonenumber']

        if not course.active == True:
            raise serializers.ValidationError({'course':'Course is not active'})

        if not course.open_to_booking == True:
            raise serializers.ValidationError({"course':'Course can't booking"})
        
        if course.limit_booking == 0:
            raise serializers.ValidationError("you can't booking now")
        
        if course.number_of_student == course.limit_booking:
            course.open_to_booking = False
            course.save()
            raise serializers.ValidationError('you cant subsecript now.')

        if course.number_of_student > course.limit_booking:
            raise serializers.ValidationError('you cant subsecript now.')

        if Subscription.objects.filter(phonenumber=phonenumber, course=course).exists():
            raise serializers.ValidationError('already exist')

        return attrs

    # def create(self, validated_data):
    #     course = self.course
    #     phonenumber = validated_data['phonenumber']
    #     subscription = Subscription.objects.create(
    #         phonenumber=phonenumber, course=course)
    #     return subscription    

        

    