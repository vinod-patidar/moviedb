import random
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from api.serializers import (LoginSerializer, UserSignupSerializer, UserEditSerializer, UserPassphraseSerializer, UserSerializer,
                             GetUserByHotelSerializer, HotelIDValidationSerializer, UserUUIDValidationSerializer)
from api.common.process import responses
from api.common.messages import (
    validation_failed_message, mobile_number_already_registered_message, mobile_number_missing_message,
    mobile_number_incorrect_message, oops_message, user_updated_success_message, invalid_uuid_message,
    hotel_or_user_not_found_message, refresh_token_required_message, otp_required_message
)
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import IsAuthenticated

from api.models import User
from api.common.utils.common_functions import get_tokens_for_user
from api.common.db.queries import get_user_by_mobile, get_hotel_by_user, get_user_by_uuid, get_users_by_hotel


class UsersByHotelView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        try:
            serializer = HotelIDValidationSerializer(data=request.data)
            if serializer.is_valid():
                hotel_id = request.data.get('hotel_id')
                users = get_users_by_hotel(hotel_id)
                if users is not None:
                    serializer = GetUserByHotelSerializer(users, many=True)
                    response_data = responses.get_user_success_response(
                        serializer.data)
                    return Response(response_data, status=status.HTTP_200_OK)
                else:
                    return Response({
                        "success": False,
                        "message": hotel_or_user_not_found_message()
                    }, status=status.HTTP_404_NOT_FOUND)
            else:
                raise ValueError(validation_failed_message())

        except ValueError as ve:
            return Response({
                "success": False,
                "message": validation_failed_message(),
                "validation_details": responses.validation_errors(
                    serializer.errors
                )
            }, status=status.HTTP_400_BAD_REQUEST)

        except Exception as e:
            return Response({
                "success": False,
                "message": oops_message(),
                "error": str(e)
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
