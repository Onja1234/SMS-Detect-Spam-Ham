def predict_spam(message: str):
    """
    Fonction pure de prédiction
    """

    spam_keywords = ["win", "free", "money", "urgent", "offer"]

    for word in spam_keywords:
        if word in message.lower():
            return {
                "label": "SPAM",
                "confidence": 0.85
            }

    return {
        "label": "HAM",
        "confidence": 0.90
    }
