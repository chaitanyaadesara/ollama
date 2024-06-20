# Stage 1: Use the Ollama image from Docker Hub
FROM ollama/ollama
EXPOSE 11431
COPY llama3.sh /scripts/script.sh
RUN ["chmod", "+x", "/scripts/script.sh"]

# Run
ENTRYPOINT ["/scripts/script.sh"]
