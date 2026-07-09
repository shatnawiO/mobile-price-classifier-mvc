import tensorflow as tf
import joblib
from pathlib import Path

model = tf.keras.models.load_model(MODELS_DIR / "price_classifier.keras")
scaler = joblib.load(MODELS_DIR / "scaler.pkl")



def predict(new_data):
    probs = model.predict(new_data)
    preds = probs.argmax(axis=1)
    confidence = probs.max(axis=1)
    return preds, confidence
