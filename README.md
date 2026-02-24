NetworkSecurity - Phishing Domain Detection

An End-to-End MLOps project designed to identify phishing websites. This project integrates classical Machine Learning with modern DevOps tools like **Docker, MLflow, and AWS** for a production-ready experience.

### 🌐 Live Demo
Experience the application live on AWS: [http://16.16.27.72:8501](http://16.16.27.72:8501)

---

### 🚀 Key Features
* **Automated Pipeline:** Modular ingestion, preprocessing, and training stages.
* **Experiment Tracking:** MLflow integration for logging metrics and artifacts.
* **Real-time Prediction:** Interactive Streamlit dashboard for user inputs.
* **Containerized Deployment:** Docker support for consistent environments.
* **Cloud Hosting:** Deployed on AWS EC2 for global accessibility.

---

### 📂 Project Structure
```text
NetworkSecurity/
├── Models/          # Best trained model artifacts (.pkl)
├── artifacts/       # Data splits, scalers, and metrics.json
├── notebooks/       # Exploratory Data Analysis (EDA)
├── src/             # Modular Source Code (Ingestion, Trainer, etc.)
├── app.py           # Streamlit Web Application
├── train.py         # Training Pipeline Execution Script
├── Dockerfile       # Container Configuration
└── requirements.txt # Python Dependencies
💻 How to Run Locally
Clone the Repo:

Bash
git clone [https://github.com/rajan7838/NetworkSecurity.git](https://github.com/rajan7838/NetworkSecurity.git)
cd NetworkSecurity
Setup Environment:

Bash
conda create -p venv python=3.11 -y
conda activate ./venv
pip install -r requirements.txt
Run Application:

Bash
streamlit run app.py

Author
A Rajan – ML & MLOps Enthusiast

GitHub: https://github.com/rajan7838
LinkedIn: https://linkedin.com/in/rajan7838
