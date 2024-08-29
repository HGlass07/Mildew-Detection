import streamlit as st
import os
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
import io
from tensorflow.keras.preprocessing.image import ImageDataGenerator



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

# function to load an image subset from dir
def load_subset_data(directory, label_name, target_size=(100, 100), n_images=20):
    datagen = ImageDataGenerator(rescale=1./255)
    data_generator = datagen.flow_from_directory(
        directory,
        target_size=target_size,
        batch_size=n_images * 3, # multiply batch number to ensure 20 images consistently appear
        class_mode='binary',
        shuffle=True  
    )
    
    images, labels = next(data_generator)
    label_indices = np.where(labels == label_name)[0]
    selected_images = images[label_indices][:n_images] 
    
    return selected_images, labels

# function to create montage
def create_montage(images, label_name, n_images=20, montage_size=(5, 4), save_path=None):
    fig, axes = plt.subplots(montage_size[1], montage_size[0], figsize=(12, 10))
    axes = axes.flatten()
    
    for img, ax in zip(images, axes):
        ax.imshow(img)
        ax.axis('off')
    
    plt.suptitle(f"Montage of {n_images} Images for Label {label_name}", fontsize=16)
    
    st.pyplot(fig)
    plt.close(fig)