from html.parser import HTMLParser


class SimpleHTMLParser(HTMLParser):
    def __init__(self) -> None:
        self.texts: list[str] = []
        HTMLParser.__init__(self)

    def handle_data(self, data: str) -> None:
        if data.strip():
            self.texts.append(data.strip())

    def get_raw_text(self) -> str:
        print(self.texts)
        return " ".join(self.texts)


def remove_tags(html_text: str) -> str:
    parser = SimpleHTMLParser()
    parser.feed(html_text)
    return parser.get_raw_text()
