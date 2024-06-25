from django.urls import path
from .views import RecommendView, ExerciseListView, ExerciseDetailView, AuthenticatedExerciseListView

urlpatterns = [
    path('recommend/', RecommendView.as_view(), name='recommend'),
    path('exercises/', ExerciseListView.as_view(), name='exercises'),
    path('exercises/<int:exercise_id>/', ExerciseDetailView.as_view(), name='exercise_detail'),
    path('authenticated_exercises/', AuthenticatedExerciseListView.as_view(), name='authenticated_exercises'),
]
