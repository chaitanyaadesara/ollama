# Use Node.js base image with a specified version
FROM node:16-alpine

# Create app directory
WORKDIR /usr/src/app

# Install app dependencies
COPY package*.json ./
RUN npm install

# Bundle app source
COPY . .

# Expose port 5000
EXPOSE 5000

# Command to run the server
CMD ["node", "ollama_app.js"]