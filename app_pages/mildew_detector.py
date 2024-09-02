import streamlit as st
from tensorflow.keras.models import load_model
from PIL import Image
import pandas as pd
import base64
from src.data_management import load_and_prep_image
from src.data_management import predict_on_images


def mildew_detector_body():

    st.info(
        f" New cherry leaf images can be uploaded below in order to "
        "use the model to predict whether powdery mildew is present. "
        "Uploaded files must be image files. Multiple files can be "
        "uploaded at once.")

    st.write("The dataset for prediction can be downloaded [here](https://www.kaggle.com/datasets/henryglasspool/cherry-leaves)")

    st.title("Image Uploader")

    #load model
    model = load_model("outputs/v1/mildew_detector_model.h5")
    
    uploaded_files = st.file_uploader("Choose images...", type=["jpg", "png", "jpeg"], accept_multiple_files=True)
    
    if uploaded_files:
        images = [Image.open(file) for file in uploaded_files]
        
        st.image(images, caption=[file.name for file in uploaded_files], use_column_width=True)
        
        predictions = predict_on_images(images, model)

        report_dataframe = pd.DataFrame(columns=["Name", "Result", "Probability"])
        
        for i, prediction in enumerate(predictions):
            label = "Healthy" if prediction < 0.5 else "Infected"
            probability = 1 - prediction if label == "Healthy" else prediction
            st.write(f"Image {uploaded_files[i].name} is predicted to be: **{label}** with a probability of **{probability:.4f}**")

            report_dataframe = report_dataframe.append({
                "Name": uploaded_files[i].name,
                "Result": label,
                "Probability": f"{probability:.4f}"
            }, ignore_index=True)

        #convert to cvs and encode to base64 for download
        csv_report = report_dataframe.to_csv(index=False)

        b64 = base64.b64encode(csv_report.encode()).decode()
        href = f'<a href="data:file/csv;base64,{b64}" download="mildew_detection_report.csv">Download Report</a>'

        st.markdown(href, unsafe_allow_html=True)
