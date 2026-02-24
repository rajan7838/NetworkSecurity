from src.components.data_ingestion import DataIngestion
from src.components.data_preprocessing import DataPreprocessing
from src.components.model_trainer import ModelTrainer
from src.components.model_evaluation import ModelEvaluation
from src.components.model_pusher import ModelPusher

if __name__ == "__main__":

    ingestion = DataIngestion()
    train_path, test_path = ingestion.initiate("data/phisingData.csv")

    preprocessing = DataPreprocessing()
    X_train, X_test, y_train, y_test = preprocessing.transform(train_path, test_path)

    trainer = ModelTrainer()
    model = trainer.train(X_train, y_train, X_test, y_test)

    evaluator = ModelEvaluation()
    evaluator.evaluate(model, X_test, y_test)

    pusher = ModelPusher()
    pusher.save(model)

    print("Full Training Pipeline Completed")

