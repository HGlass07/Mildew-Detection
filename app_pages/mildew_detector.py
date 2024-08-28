import streamlit as st
import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import img_to_array
from PIL import Image
import pandas as pd
import base64

# load and preprocess an image
def load_and_prep_image(image, target_size=(100, 100)):
    image = image.resize(target_size)
    image = img_to_array(image)
    image = image / 255.0 
    image = np.expand_dims(image, axis=0)
    return image

# predict on uploaded images
def predict_on_images(images, model):
    predictions = []
    for image in images:
        img_array = load_and_prep_image(image)
        prediction = model.predict(img_array)
        predictions.append(prediction[0][0])
    return predictions

def mildew_detector_body():
    st.title("Image Uploader")

    # load model
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

        # convert to cvs and encode to base64 for download
        csv_report = report_dataframe.to_csv(index=False)

        b64 = base64.b64encode(csv_report.encode()).decode()
        href = f'<a href="data:file/csv;base64,{b64}" download="mildew_detection_report.csv">Download Report</a>'

        st.markdown(href, unsafe_allow_html=True)
