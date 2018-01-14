from rest_framework.generics import ListAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView, CreateAPIView

from .serializers import UserCreateSerializer, UserActivateSerializer, UserLoginSerializer
#, UserLoginSerializer

from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser, IsAuthenticatedOrReadOnly

#from posts.api.permissions import IsOwnerOrReadOnly

from rest_framework.filters import SearchFilter, OrderingFilter

from django.db.models import Q

#from posts.api.paginations import PostLimitOffsetPagination, PostPageNumberPagination

from rest_framework.mixins import DestroyModelMixin, UpdateModelMixin

from django.contrib.auth import get_user_model

from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
from rest_framework.views import APIView

from user.models import UserProfile

User = get_user_model()

# Create your views here.

class UserCreateAPIView(CreateAPIView):
	serializer_class = UserCreateSerializer
	queryset = User.objects.all()

class UserActivateAPIView(RetrieveAPIView):
	serializer_class = UserActivateSerializer
	queryset = UserProfile.objects.all()


class UserLoginAPIView(APIView):
	serializer_class = UserLoginSerializer
	permission_classes = [AllowAny]


	def post(self, request, *args, **kwargs):
		data = request.data
		serializer = UserLoginSerializer(data=data)
		if serializer.is_valid(raise_exception=True):
			new_data = serializer.data
			return Response(new_data, status=HTTP_200_OK)
		return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)	



