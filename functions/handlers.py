from html_cleaner import remove_tags


def clean_text(event: dict, context: dict) -> dict:
    return {"cleaned_text": remove_tags(event["html_text"])}
