from sklearn.metrics import classification_report, accuracy_score
import json
import os


class ModelEvaluation:

    def evaluate(self, model, X_test, y_test):

        preds = model.predict(X_test)

        accuracy = accuracy_score(y_test, preds)

        report = classification_report(
            y_test,
            preds,
            output_dict=True,
            zero_division=0
        )

        metrics = {
            "accuracy": accuracy,
            "classification_report": report
        }

        os.makedirs("artifacts", exist_ok=True)

        file_path = os.path.join(
            "artifacts",
            f"metrics_{model.__class__.__name__}.json"
        )

        with open(file_path, "w") as f:
            json.dump(metrics, f, indent=4)

        return metrics  