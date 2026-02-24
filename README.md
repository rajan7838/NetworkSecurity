##NetworkSecurity – Phishing Domain Detection

An End-to-End MLOps project designed to identify phishing websites. This project integrates classical Machine Learning with modern DevOps tools like Docker, MLflow, and AWS for a production-ready experience.

 Experience the application live on AWS: http://16.16.27.72:8501

Key Features
Automated Pipeline: Modular ingestion, preprocessing, and training stages.

Experiment Tracking: MLflow integration for logging metrics, parameters, and model artifacts.

Real-time Prediction: Interactive Streamlit dashboard for user inputs.

Containerized Deployment: Docker support for consistent environments.

Cloud Hosting: Deployed on AWS EC2 for global accessibility.

Robustness: Custom logging and exception handling with full traceback.

Project Structure
Plaintext
NetworkSecurity/
├── src/                # Modular Source Code (Ingestion, Trainer, Logger, Exception)
├── models/             # Best trained model artifacts (.pkl)
├── artifacts/          # Data splits, scalers, and metrics.json
├── notebooks/          # Exploratory Data Analysis (EDA)
├── app.py              # Streamlit Web Application
├── train.py            # Training Pipeline Execution Script
├── Dockerfile          # Container Configuration
└── requirements.txt    # Python Dependencies
Setup & Execution
1. Installation
Bash
git clone https://github.com/rajan7838/NetworkSecurity.git
cd NetworkSecurity
conda create -p venv python=3.11 -y && conda activate ./venv
pip install -r requirements.txt
2. Run Locally
Train Model: python train.py

Launch App: streamlit run app.py

3. Docker Deployment
Bash
docker build -t phishing-app .
docker run -p 8501:8501 phishing-app

Tech Stack
ML: Scikit-learn (RandomForest, GradientBoosting), Pandas, Numpy.

MLOps: MLflow, Docker.

Cloud: AWS EC2 (Ubuntu 22.04).

UI: Streamlit.

Metrics & Evaluation
Models are optimized via GridSearchCV and tracked in MLflow. Final metrics (Accuracy, Precision, F1-Score) are stored in artifacts/metrics.json.

Author
A Rajan – ML & MLOps Enthusiast

GitHub: https://github.com/rajan7838
LinkedIn: https://linkedin.com/in/rajan7838