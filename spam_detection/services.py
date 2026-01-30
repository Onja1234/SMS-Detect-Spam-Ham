import joblib
import re
from pathlib import Path
from django.conf import settings

# Charger le modèle et le vectorizer au démarrage (une seule fois)
MODEL_DIR = Path(settings.BASE_DIR) / "spam_detection" / 'ml_models' 

try:
    model = joblib.load(MODEL_DIR / 'spam_detector_model.pkl')
    vectorizer = joblib.load(MODEL_DIR / 'tfidf_vectorizer.pkl')
    MODEL_LOADED = True
except Exception as e:
    print(f"Erreur lors du chargement du modèle: {e}")
    MODEL_LOADED = False


def clean_text(text):
    """
    Nettoie le texte en:
    - Convertissant en minuscules
    - Supprimant les URLs
    - Supprimant les numéros de téléphone
    - Supprimant les chiffres excessifs
    - Supprimant la ponctuation excessive
    - Supprimant les espaces multiples
    """
    # Convertir en minuscules
    text = text.lower()

    # Supprimer les URLs
    text = re.sub(r'http\S+|www\S+', '', text)

    # Supprimer les numéros de téléphone
    text = re.sub(r'\+?\d[\d\s-]{8,}', '', text)

    # Supprimer les caractères spéciaux tout en gardant les lettres accentuées
    text = re.sub(r'[^a-zàâäéèêëïîôùûüÿçœæ\s]', ' ', text)

    # Supprimer les espaces multiples
    text = re.sub(r'\s+', ' ', text).strip()

    return text


def predict_spam(message: str):
    """
    Fonction de prédiction utilisant le modèle ML
    
    Args:
        message (str): Le texte du message à analyser
        
    Returns:
        dict: {"label": "SPAM" ou "HAM", "confidence": float}
    """
    if not MODEL_LOADED:
        # Fallback si le modèle n'est pas chargé
        return {
            "label": "HAM",
            "confidence": 0.5,
            "error": "Model not loaded"
        }
    
    try:
        # 1. Nettoyer le texte
        cleaned_message = clean_text(message)
        
        # 2. Vectoriser le texte
        message_vectorized = vectorizer.transform([cleaned_message])
        
        # 3. Prédire avec probabilités
        prediction = model.predict(message_vectorized)[0]
        probabilities = model.predict_proba(message_vectorized)[0]
        
        # 4. Déterminer le label et la confidence
        label = "SPAM" if prediction == 1 else "HAM"
        confidence = float(max(probabilities))
        
        return {
            "label": label,
            "confidence": round(confidence, 2)
        }
        
    except Exception as e:
        print(f"Erreur lors de la prédiction: {e}")
        return {
            "label": "HAM",
            "confidence": 0.5,
            "error": str(e)
        }