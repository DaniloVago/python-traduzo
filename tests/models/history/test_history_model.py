import json
from src.models.history_model import HistoryModel


# Req. 7
def test_request_history():
    history_json = HistoryModel.list_as_json()
    history_data = json.loads(history_json)

    expected_data = [
        {"text_to_translate": "Hello, I like videogame",
         "translate_from": "en",
         "translate_to": "pt"},
        {"text_to_translate": "Do you love music?",
         "translate_from": "en",
         "translate_to": "pt"},
    ]

    for entry in history_data:
        del entry["_id"]

    assert history_data == expected_data
