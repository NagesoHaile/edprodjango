
from rest_framework import generics
from .models import Member, Admin, Event, Contribution, Benefit, Profile, MemberFamily
from .serializers import MemberSerializer, AdminSerializer, EventSerializer, ContributionSerializer, BenefitSerializer, ProfileSerializer, MemberFamilySerializer


# Generic views for the Member Model
class MemberListCreateView(generics.ListCreateAPIView):
    queryset = Member.objects.all()
    serializer_class = MemberSerializer

class MemberDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Member.objects.all()
    serializer_class = MemberSerializer

# Generic views for the Admin Model
class AdminListCreateView(generics.ListCreateAPIView):
    queryset = Admin.objects.all()
    serializer_class = AdminSerializer

class AdminDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Admin.objects.all()
    serializer_class = AdminSerializer


# Generic views for the Event Model
class EventListCreateView(generics.ListCreateAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer

class EventDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer

# Generic views for the Contribution Model
class ContributionListCreateView(generics.ListCreateAPIView):
    queryset = Contribution.objects.all()
    serializer_class = ContributionSerializer

class ContributionDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Contribution.objects.all()
    serializer_class = ContributionSerializer

# Generic views for the Benefit Model
class BenefitListCreateView(generics.ListCreateAPIView):
    queryset = Benefit.objects.all()
    serializer_class = BenefitSerializer

class BenefitDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Benefit.objects.all()
    serializer_class = BenefitSerializer

# Generic views for the Profile Model
class ProfileListCreateView(generics.ListCreateAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

class ProfileDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

# Generic views for the MemberFamily Model
class MemberFamilyListCreateView(generics.ListCreateAPIView):
    queryset = MemberFamily.objects.all()
    serializer_class = MemberFamilySerializer

class MemberFamilyDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = MemberFamily.objects.all()
    serializer_class = MemberFamilySerializer

