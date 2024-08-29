import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
import joblib

def load_pkl_file(file_path):
    return joblib.load(filename=file_path)

def load_test_evaluation(version):
    return load_pkl_file(f'outputs/{version}/model_evaluation.pkl')