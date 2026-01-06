# Use a lightweight Python version
FROM python:3.9-slim

# Set working directory inside container
WORKDIR /app

# Copy dependency file first (for caching)
COPY requirements.txt .

# Install dependencies
# We also update pip to ensure smooth installation
RUN pip install --upgrade pip && \
    pip install -r requirements.txt

# Copy the rest of the app code
COPY . .

# Expose Streamlit's default port
EXPOSE 8501

# Command to run the app
CMD ["streamlit", "run", "app.py", "--server.address=0.0.0.0"]