import random

from html_cleaner import remove_tags


def clean_text(event: dict, context: dict) -> str:
    return remove_tags(event["html_text"])


def create_embedding(event: dict, context: dict) -> list[float]:
    return random.sample(range(0, 100), 50)


def predict_salary(event: dict, context: dict) -> int:
    return random.randint(50000, 1000000)
