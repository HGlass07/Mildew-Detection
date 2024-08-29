import streamlit as st
import os
from PIL import Image
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from src.data_management import load_subset_data
from src.data_management import create_montage

def leaves_visualiser_body():
    st.title("Leaf Image Visualisations")

    st.info(
        f"Below are the results of the study to visualise the " 
        "difference between healthy and unhealthy leaves. Displayed are: ")

    st.success (f"* Images showing the mean and variability of images in both sets. ")
    st.success (f"* Images illustrating the differences between average healthy. "
                "and unhealthy leaves.")  
    st.success (f"* An image montage selector with both sets. ") 

    # display Mean and Variability Images
    st.header("Mean and Variability Images")

    variability_image_label_0 = Image.open("outputs/v1/variability_image_label_0.png")
    variability_image_label_1 = Image.open("outputs/v1/variability_image_label_1.png")

    st.subheader("Healthy Leaves (Label 0)")
    st.image(variability_image_label_0, caption="Mean and Variability Image - Healthy", use_column_width=True)

    st.subheader("Infected Leaves (Label 1)")
    st.image(variability_image_label_1, caption="Mean and Variability Image - Infected", use_column_width=True)

    # display Difference Image
    st.header("Difference Image Between Infected and Healthy Leaves")
    difference_image = Image.open("outputs/v1/avg_infected_uninfected_diff.png")
    st.image(difference_image, caption="Difference Image", use_column_width=True)

    # display montage
    st.header("Montage Generator")
    label_selection = st.selectbox("Select Leaf Type for Montage:", ("Healthy (Label 0)", "Infected (Label 1)"))

    if st.button("Generate Montage"):
        data_dir = "inputs/cherry-leaves/cherry-leaves/validation"
        if label_selection == "Healthy (Label 0)":
            label = 0
        else:
            label = 1
        
        val_images, val_labels = load_subset_data(data_dir, label_name=label, n_images=20)
        
        create_montage(val_images, label_name=label)

