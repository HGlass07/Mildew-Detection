import streamlit as st
from app_pages.multipage import MultiPage

# load pages scripts
from app_pages.project_summary import project_summary_body
from app_pages.leaves_visualiser import leaves_visualiser_body
from app_pages.mildew_detector import mildew_detector_body
from app_pages.model_performance import model_performance_body

app = MultiPage(app_name="Mildew Detector")  # Create instance

# Add app pages
app.add_page("Project Summary", project_summary_body)
app.add_page("Leaves Visualiser",leaves_visualiser_body)
app.add_page("Mildew Detection", mildew_detector_body)
app.add_page("ML Performance", model_performance_body)

app.run()  # Run app
