import pandas as pd
import joblib
from sklearn.preprocessing import StandardScaler
from src.config import Config

class DataPreprocessing:

    def transform(self, train_path, test_path):

        train_df = pd.read_csv(train_path)
        test_df = pd.read_csv(test_path)

        X_train = train_df.drop("Result", axis=1)
        y_train = train_df["Result"]

        X_test = test_df.drop("Result", axis=1)
        y_test = test_df["Result"]

        scaler = StandardScaler()

        X_train = scaler.fit_transform(X_train)
        X_test = scaler.transform(X_test)

        joblib.dump(scaler, Config.SCALER_PATH)

        return X_train, X_test, y_train, y_test
