import requests

WGER_API_URL = "https://wger.de/api/v2/"

def get_exercises():
    response = requests.get(f"{WGER_API_URL}exercise/")
    if response.status_code == 200:
        return response.json()
    else:
        return None

def get_exercise_by_id(exercise_id):
    response = requests.get(f"{WGER_API_URL}exercise/{exercise_id}/")
    if response.status_code == 200:
        return response.json()
    else:
        return None

def authenticate(username, password):
    data = {'username': username, 'password': password}
    response = requests.post(f"{WGER_API_URL}token/", data=data)
    if response.status_code == 200:
        return response.json()
    else:
        return None

def get_authenticated_exercises(access_token):
    headers = {'Authorization': f'Bearer {access_token}'}
    response = requests.get(f"{WGER_API_URL}workout/", headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        return None
