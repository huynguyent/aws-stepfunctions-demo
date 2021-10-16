from functions import html_cleaner


def test_remove_tags() -> None:
    html_text = """<html><head><title>Test</title></head>
                <body><h1>Parse me!</h1></body></html>"""
    cleaned_text = html_cleaner.remove_tags(html_text)

    assert cleaned_text == "Test Parse me!"
