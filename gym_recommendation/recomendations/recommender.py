import pandas as pd
from sklearn.neighbors import NearestNeighbors
from .models import UserPreference

class Recommender:
    def __init__(self):
        self.model = None
        self.data = None
        self.fit()

    def fit(self):
        preferences = UserPreference.objects.all().values()
        df = pd.DataFrame(preferences)
        if df.empty:
            return
        self.data = df.set_index('user_id')
        self.model = NearestNeighbors(metric='cosine', algorithm='brute')
        self.model.fit(self.data)

    def get_recommendations(self, user_id, n_recommendations=3):
        if self.model is None or self.data is None:
            return []
        user_index = self.data.index[self.data.index == user_id].tolist()[0]
        distances, indices = self.model.kneighbors(self.data.iloc[user_index, :].values.reshape(1, -1), n_neighbors=n_recommendations+1)
        recommendations = indices.flatten()[1:]
        return self.data.iloc[recommendations].index.tolist()

recommender = Recommender()
