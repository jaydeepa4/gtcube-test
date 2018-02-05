from rest_framework.generics import ListAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView, CreateAPIView, RetrieveUpdateAPIView

from .serializers import SellerCreateSerializer, SellerActivateSerializer, SellerProfileSerializer, SellerDetailSerializer, UserEmailSerializer
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

from seller.models import SellerProfile, UserEmail

from rest_framework.parsers import MultiPartParser, FormParser

User = get_user_model()

# Create your views here.

class SellerCreateAPIView(CreateAPIView):
	serializer_class = SellerCreateSerializer
	queryset = User.objects.all()
	permission_classes = [AllowAny]


class UserEmailAPIView(CreateAPIView):
	serializer_class = UserEmailSerializer
	queryset = UserEmail.objects.all()
	permission_classes = [AllowAny]


class SellerActivateAPIView(RetrieveAPIView):
	serializer_class = SellerActivateSerializer
	queryset = SellerProfile.objects.all()
	permission_classes = [AllowAny]
	


# class SellerLoginAPIView(APIView):
# 	serializer_class = SellerLoginSerializer
# 	permission_classes = [AllowAny]


# 	def post(self, request, *args, **kwargs):
# 		data = request.data
# 		serializer = SellerLoginSerializer(data=data)
# 		if serializer.is_valid(raise_exception=True):
# 			new_data = serializer.data
# 			return Response(new_data, status=HTTP_200_OK)
# 		return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)	


class SellerProfileAPIView(UpdateModelMixin, RetrieveAPIView):
	serializer_class = SellerProfileSerializer
	queryset = SellerProfile.objects.all()
	permission_classes = [AllowAny]
	# parser_classes = (MultiPartParser, FormParser,)


	def put(self, request, *args, **kwargs):
		data = request.data
		serializer = SellerProfileSerializer(data=data)
		if serializer.is_valid(raise_exception=True):
			new_data = serializer.data
			return Response(new_data, status=HTTP_200_OK)
		return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)	
		# kwargs['partial'] = True
  #       return self.update(request, *args, **kwargs)

   


class SellerDetailAPIView(RetrieveAPIView):
	serializer_class = SellerDetailSerializer
	queryset = SellerProfile.objects.all()
	lookup_field = 'email'
	permission_classes = [AllowAny]
