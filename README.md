# 🚦 Intelligent Detection of Traffic Rule Violations Using Computer Vision

![Python](https://img.shields.io/badge/Python-3.11-blue) ![YOLOv8](https://img.shields.io/badge/YOLOv8-Ultralytics-orange) ![Flask](https://img.shields.io/badge/Flask-2.3-green) ![Streamlit](https://img.shields.io/badge/Streamlit-1.24-red)

## Problem Statement
Traffic violations such as helmetless riding and red-light jumping are major causes of road accidents. Manual monitoring through CCTV cameras is inefficient and prone to human error. This project proposes a computer vision and machine learning system that can automatically detect traffic violations in real time and assist authorities in enforcing road safety.

## Objectives
- Collect and preprocess traffic video data for analysis
- Apply computer vision (YOLO + OpenCV) for detecting vehicles, helmets, and traffic signals
- Implement rule-based logic for identifying violations (helmetless riding, red-light jumping)
- Integrate OCR (Tesseract) for automatic number plate recognition
- Store violation details in a database and display them in a web application
- Evaluate system accuracy and reliability in real-world scenarios

## Tools & Technologies
- Python
- OpenCV, YOLOv8 (Ultralytics), Tesseract OCR, Pandas, NumPy
- MySQL / SQLite
- Flask / Streamlit
- Matplotlib, Seaborn

## Project Structure
See PROJECT_FLOW.md

## Workflow
1. Data Collection → Scrape/download videos/images
2. Data Annotation → Label helmets, vehicles, traffic lights
3. Model Training → Fine-tune YOLOv8 with custom dataset
4. Evaluation → Measure accuracy, precision, recall, F1-score
5. Deployment → Web app (Flask/Streamlit) + database storage
6. Maintenance → Expand dataset, retrain, improve accuracy

## Expected Outcomes
- Automated detection of helmetless riding and red-light jumping
- Image snapshots of violators with extracted number plate details
- A structured database of violations accessible via a simple dashboard
- Contribution toward smart city traffic management and road safety
