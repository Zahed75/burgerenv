from rest_framework.viewsets import ModelViewSet
from .models import *
from .serializers import *
from rest_framework.permissions import IsAuthenticated


# Create your views here.

class UserProfileViewSet(ModelViewSet):
    serializer_class = UserProfileSerializer
    queryset = UserProfile.objects.all()


class OrderViewSet(ModelViewSet):
    serializer_class = OrderSerializer
    permission_classes = [
        IsAuthenticated,
    ]

    # queryset = Order.objects.all() # whenever you write get queryset method you dont have to need this

    # filtering section order filter

    def get_queryset(self):
        queryset = Order.objects.all()
        id = self.request.query_params.get("id", None)
        if id is not None:
            queryset = queryset.filter(user__id=id)
        return queryset

# ?id=2
