import datetime
import json
import pickle

import pandas as pd
import requests
import streamlit


def run():
    streamlit.title("Sarcasm Prediction 🙃 Vs 😑")
    hi = streamlit.text_input("Your Sentence ", "")
    
    # name = 'model' + '.pkl'
    # model = pickle.load(open(name,'rb'))

    # if streamlit.button("Predict"):
    #     prediction = model.predict([hi])
    #     streamlit.success(f"Cluster Number: {prediction}")
        # streamlit.success(f"Coordinates:  {model.cluster_centers_[prediction]}")
    

if __name__ == '_main_':

    #by default it will run at 8501 port
    run()