import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
from src.machine_learning.evaluation import load_test_evaluation

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