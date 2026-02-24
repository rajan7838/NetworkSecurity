import streamlit as st
import joblib
import numpy as np


model = joblib.load("Models/best_model.pkl")

st.title("Phishing Website Detection App")

st.write("Enter feature values (0 = No, 1 = Yes)")


feature_names = [
    "having_IP_Address",
    "URL_Length",
    "Shortining_Service",
    "having_At_Symbol",
    "double_slash_redirecting",
    "Prefix_Suffix",
    "having_Sub_Domain",
    "SSLfinal_State",
    "Domain_registeration_length",
    "Favicon",
    "port",
    "HTTPS_token",
    "Request_URL",
    "URL_of_Anchor",
    "Links_in_tags",
    "SFH",
    "Submitting_to_email",
    "Abnormal_URL",
    "Redirect",
    "on_mouseover",
    "RightClick",
    "popUpWidnow",
    "Iframe",
    "age_of_domain",
    "DNSRecord",
    "web_traffic",
    "Page_Rank",
    "Google_Index",
    "Links_pointing_to_page",
    "Statistical_report"
]

# Input fields
features = []
for feature in feature_names:
    value = st.number_input(feature, min_value=-1, max_value=1, step=1)
    features.append(value)

# Prediction button
if st.button("Predict"):
    input_data = np.array(features).reshape(1, -1)
    prediction = model.predict(input_data)

    if prediction[0] == 1:
        st.success("Legitimate Website")
    else:
        st.error("Phishing Website Detected")