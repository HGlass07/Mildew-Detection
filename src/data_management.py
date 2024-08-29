import streamlit as st
import os
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
import io
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.preprocessing.image import img_to_array


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