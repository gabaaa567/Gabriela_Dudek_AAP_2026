import re

POS_WORDS = {"good","great","excellent","wonderful","love","best","amazing","brilliant","perfect"}
NEG_WORDS = {"bad","worst","awful","terrible","hate","boring","waste","poor","horrible"}

def sentiment_score(text: str) -> int:
    words = re.findall(r"\w+", text.lower())

    score = 0

    for word in words:
        if word in POS_WORDS:
            score += 1
        elif word in NEG_WORDS:
            score -= 1

    return score
