# ------------------------------
# Stage 1: Base image
# ------------------------------
FROM python:3.10-slim

# Set working directory inside container
WORKDIR /app

# Copy project files into the container
COPY . /app

# Install system dependencies for OpenCV & Tesseract
RUN apt-get update && apt-get install -y \
    tesseract-ocr \
    libgl1-mesa-glx \
    libglib2.0-0 \
    && apt-get clean

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose a port (for Flask dashboard later)
EXPOSE 5000

# Run a default command (can be changed later)
CMD ["python", "src/number_plate_ocr.py"]

