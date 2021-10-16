from html_cleaner import remove_tags


def clean_text(event: dict, context: dict) -> str:
    return remove_tags(event["html_text"])
