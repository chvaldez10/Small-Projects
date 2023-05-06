import requests

APRI_URL = "https://opentdb.com/api.php"

def get_data_from_api(parameters_from_user) -> list[dict]:
    trivia_response_data = requests.get(url=APRI_URL, params=parameters_from_user)
    trivia_response_data.raise_for_status()
    trivia_data = trivia_response_data.json()

    return trivia_data["results"]