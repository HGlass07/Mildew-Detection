import streamlit as st
from PIL import Image


def leaves_visualiser_body():
    st.write("This is page 2")
    st.title("Leaf Image Visualisations")

    # Display Mean and Variability Images
    st.header("Mean and Variability Images")

    variability_image_label_0 = Image.open("outputs/v1/variability_image_label_0.png")
    variability_image_label_1 = Image.open("outputs/v1/variability_image_label_1.png")

    st.subheader("Healthy Leaves (Label 0)")
    st.image(variability_image_label_0, caption="Variability Image - Healthy", use_column_width=True)

    st.subheader("Infected Leaves (Label 1)")
    st.image(variability_image_label_1, caption="Variability Image - Infected", use_column_width=True)

    # Display Difference Image
    st.header("Difference Image Between Infected and Healthy Leaves")
    difference_image = Image.open("outputs/v1/avg_infected_uninfected_diff.png")
    st.image(difference_image, caption="Difference Image", use_column_width=True)


