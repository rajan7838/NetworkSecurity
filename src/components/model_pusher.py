import joblib
import os
from src.config import Config

class ModelPusher:

    def save(self, model):
        os.makedirs("models", exist_ok=True)
        joblib.dump(model, Config.MODEL_PATH)