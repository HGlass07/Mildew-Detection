import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
import joblib

def load_pkl_file(file_path):
    return joblib.load(filename=file_path)

def load_test_evaluation(version):
    return load_pkl_file(f'outputs/{version}/model_evaluation.pkl')

def model_performance_body():
    version = 'v1'

    st.write("## Train, Validation and Test Set: Labels Frequencies")

    labels_distribution = plt.imread(f"outputs/{version}/labels_distribution.png")
    st.image(labels_distribution, caption='Labels Distribution on Train, Validation and Test Sets')
    st.write("---")


    st.write("## Model Performance Specifics")
    st.write("### Accuracy")
    model_acc = plt.imread(f"outputs/{version}/accuracy_plot.png")
    st.image(model_acc, caption='Model Training Accuracy')
    st.write("### Loss")
    model_loss = plt.imread(f"outputs/{version}/loss_plot.png")
    st.image(model_loss, caption='Model Training Losses')
    st.write("---")

    st.write("### Generalised Performance on Test Set")
    st.dataframe(pd.DataFrame(load_test_evaluation(version), index=['Loss', 'Accuracy']))