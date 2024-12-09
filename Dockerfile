# Use the official Python image
FROM python:3.9-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements file and install dependencies
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copy the rest of the application into the container
COPY . .

# Expose port 5000
EXPOSE 5000

# Run the server when the container starts
CMD ["python", "app.py"]