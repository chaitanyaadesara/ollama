FROM ubuntu:20.04

# Install necessary packages
RUN apt-get update && apt-get install -y \
    curl \
    nodejs \
    npm


# Copy the Flask app to the container
COPY ollama_app.js /app/ollama_app.js
COPY package.json /app/package.json

# Install Flask
RUN cd app
RUN npm i
# Expose the port the app runs on
EXPOSE 5000

# Run the Flask app
CMD ["node", "ollama_app.js"]
