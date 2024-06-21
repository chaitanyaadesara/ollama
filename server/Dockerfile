FROM ubuntu:20.04

# Install necessary packages
RUN apt-get update && apt-get install -y \
    curl \
    nodejs

# Install Flask
RUN npm i express axios

# Copy the Flask app to the container
COPY ollama_app.js /app/ollama_app.js

# Expose the port the app runs on
EXPOSE 5000

# Run the Flask app
CMD ["node", "/app/ollama_app.js"]
