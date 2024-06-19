FROM ubuntu:20.04

# Install necessary packages
RUN apt-get update && apt-get install -y \
    curl \
    python3 \
    python3-pip

# Install Flask
RUN pip3 install Flask requests

# Copy the Flask app to the container
COPY ollama_app.py /app/ollama_app.py

# Expose the port the app runs on
EXPOSE 5000

# Run the Flask app
CMD ["python3", "/app/app.py"]
