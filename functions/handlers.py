from . import html_cleaner


def hello(event: dict, context: dict) -> dict:
    return {"cleaned_text": html_cleaner.remove_tags(event["html_text"])}
