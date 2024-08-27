import streamlit as st
from app_pages.multipage import MultiPage

# load pages scripts
from app_pages.page_project_summary import page_project_summary_body
from app_pages.page_leaves_visualiser import page_leaves_visualiser_body
from app_pages.page_mildew_detector import page_mildew_detector_body
from app_pages.page_model_performance import model_performance_body

app = MultiPage(app_name="Mildew Detector")  # Create instance

# Add app pages
app.add_page("Project Summary", page_project_summary_body)
app.add_page("Leaves Visualiser", page_leaves_visualiser_body)
app.add_page("Mildew Detection", page_mildew_detector_body)
app.add_page("ML Performance", model_performance_body)

app.run()  # Run app
