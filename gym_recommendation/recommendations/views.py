from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .recommender import recommender

class RecommendView(APIView):
    def get(self, request, format=None):
        user_id = int(request.query_params.get('user_id'))
        recommendations = recommender.get_recommendations(user_id)
        return Response(recommendations, status=status.HTTP_200_OK)

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .wger_api import get_exercises, get_exercise_by_id, authenticate, get_authenticated_exercises

class ExerciseListView(APIView):
    def get(self, request, format=None):
        exercises = get_exercises()
        if exercises:
            return Response(exercises, status=status.HTTP_200_OK)
        else:
            return Response({"error": "Unable to fetch exercises"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class ExerciseDetailView(APIView):
    def get(self, request, exercise_id, format=None):
        exercise = get_exercise_by_id(exercise_id)
        if exercise:
            return Response(exercise, status=status.HTTP_200_OK)
        else:
            return Response({"error": "Unable to fetch exercise"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class AuthenticatedExerciseListView(APIView):
    def post(self, request, format=None):
        username = request.data.get('username')
        password = request.data.get('password')
        tokens = authenticate(username, password)
        if tokens:
            access_token = tokens.get('access')
            exercises = get_authenticated_exercises(access_token)
            if exercises:
                return Response(exercises, status=status.HTTP_200_OK)
            else:
                return Response({"error": "Unable to fetch authenticated exercises"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        else:
            return Response({"error": "Authentication failed"}, status=status.HTTP_401_UNAUTHORIZED)

