from rest_framework import serializers
from .models import Member, Admin, Event, Contribution, Benefit, Profile, MemberFamily


class MemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Member
        fields =  '__all__'

# Serializer for the Admin Model
class AdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = Admin
        fields = '__all__'

# Serializer for the Event Model
class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = '__all__'

# Serializer for the Contribution Model
class ContributionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contribution
        fields = '__all__'

# Serializer for the Benefit Model
class BenefitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Benefit
        fields = '__all__'

# Serializer for the Profile Model
class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'

# Serializer for the MemberFamily Model
class MemberFamilySerializer(serializers.ModelSerializer):
    class Meta:
        model = MemberFamily
        fields = '__all__'