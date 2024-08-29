import streamlit as st


def project_summary_body():

    st.write("### Project Background")
    st.info(
        f"The cherry plantation crop from Farmy & Foods is facing a challenge " 
        f"where their cherry plantations have been presenting powdery mildew. " 
        f"Currently, the process is manual verification if a given cherry tree "
        f"contains powdery mildew. To save time, the IT team has suggested "
        f"that a machine learning system could be used to detect the pressence "
        f"of mildew on leaf images\n\n"
        f"**Business Requirements: **\n\n"
        f"- The client is interested in conducting a study to visually differentiate "
        "a healthy cherry leaf from one with powedery mildew.\n"
        f"- The client is interested in predicting if a cherry leaf is healthy or "
        f" contains powdery mildew.")

    st.write("### Hypothesis")
    st.info(
        f"As the leaves of cherry trees can be manually differentiated by the " 
        f"visible presence of powdery mildew, it is believed that a classification "
        f"machine learning model can expedite this process by instantly discerning " 
        f"if mildew is present on a leaf. This would be achieved through an "
        f"average image study, with the accuracy of the model informing the "
        f"validity of the hypothesis. ")

    st.write("### Conclusions and Outcomes")
    st.success(
        f"Overall the project has been successful when measured against the business "
        f"outcomes stated by the client. \n"
        f"- The leaf image study successfully visualised the mean and variability of "
        f"the images within the two sets, and was able to produce a difference image that"
        f"could be used to inform the machine learning model \n"
        f"- The machine learning model has shown to be able to differentiate between "
        f"infected and uninfected leaves with a high degree of accuracy, with the model "
        f"being potentially applicable to future datasets.")

    st.write("For additional information please see the "
    "project [README](https://github.com/HGlass07/Mildew-Detection/blob/175300c31b47db84bb3cc19d779696c606ee992b/README.md) document")


        