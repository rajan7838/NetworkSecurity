from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import GridSearchCV
import mlflow
import mlflow.sklearn

class ModelTrainer:

    def train(self, X_train, y_train, X_test, y_test):
        # --- MLFLOW SETUP ---
        mlflow.set_tracking_uri("http://127.0.0.1:5000")
        
        mlflow.set_experiment("Phishing Detection")

        mlflow.sklearn.autolog(log_datasets=False)

        models = {
            "RandomForest": (
                RandomForestClassifier(),
                {
                    "n_estimators": [100, 200],
                    "max_depth": [None, 10]
                }
            ),
            "DecisionTree": (
                DecisionTreeClassifier(),
                {
                    "max_depth": [None, 10, 20],
                    "min_samples_split": [2, 5]
                }
            ),
            "GradientBoosting": (
                GradientBoostingClassifier(),
                {
                    "n_estimators": [100, 200],
                    "learning_rate": [0.01, 0.1]
                }
            )
        }

        best_model = None
        best_accuracy = 0

        for model_name, (model, params) in models.items():
            
            with mlflow.start_run(run_name=model_name):

                grid = GridSearchCV(model, params, cv=3)
                grid.fit(X_train, y_train)

                best_estimator = grid.best_estimator_
                accuracy = best_estimator.score(X_test, y_test)

                mlflow.log_metric("test_accuracy", accuracy)
                
                mlflow.sklearn.log_model(best_estimator, f"{model_name}_model")

                if accuracy > best_accuracy:
                    best_accuracy = accuracy
                    best_model = best_estimator
                
                print(f"Finished training {model_name} with Accuracy: {accuracy:.4f}")

        return best_model          


if __name__ == "__main__":
    print("Training Started...")

    from sklearn.datasets import make_classification
    from sklearn.model_selection import train_test_split

    # Dummy data for testing
    X, y = make_classification(n_samples=1000, n_features=20)
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    trainer = ModelTrainer()
    trainer.train(X_train, y_train, X_test, y_test)
    print("Training process finished and logged to MLflow.")