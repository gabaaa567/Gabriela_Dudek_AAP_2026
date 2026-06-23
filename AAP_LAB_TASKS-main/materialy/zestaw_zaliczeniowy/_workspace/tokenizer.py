
import re

class Tokenizer:
    """Konfigurowany tokenizator: HTML strip + case + min length filter."""
    def __init__(self, lower: bool = True, strip_html: bool = True, min_length: int = 1):
        # TODO: zapisz parametry jako atrybuty self.*
        
        self.lower = lower
        self.strip_html = strip_html
        self.min_length = min_length

    def tokenize(self, text: str) -> list[str]:
        # 1. jesli self.strip_html: usun znaczniki regex r"<[^>]+>"
        # 2. jesli self.lower: text -> lowercase
        # 3. tokeny = re.findall(r"\w+", text)  (UWAGA: musi lapac polskie litery -> uzyj re.UNICODE)
        # 4. zwroc [t for t in tokeny if len(t) >= self.min_length]
        # TODO
        if self.strip_html:
            text = re.sub(r"<[^>]+>", " ", text)

        if self.lower:
            text = text.lower()

        tokens = re.findall(r"\w+", text, flags=re.UNICODE)

        result = []
        for token in tokens:
            if len(token) >= self.min_length:
                result.append(token)

        return result

    def vocab(self, texts: list[str]) -> set[str]:
        # TODO: unia tokenow ze wszystkich tekstow
        all_tokens = set()

        for text in texts:
            tokens = self.tokenize(text)
            for token in tokens:
                all_tokens.add(token)

        return all_tokens
