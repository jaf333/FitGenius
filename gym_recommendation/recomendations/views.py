from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .recommender import recommender

class RecommendView(APIView):
    def get(self, request, format=None):
        user_id = int(request.query_params.get('user_id'))
        recommendations = recommender.get_recommendations(user_id)
        return Response(recommendations, status=status.HTTP_200_OK)
