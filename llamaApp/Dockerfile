# Stage 1: Use the Ollama image from Docker Hub
FROM ollama/ollama
EXPOSE 11431
COPY script.sh /scripts/script.sh
RUN ["chmod", "+x", "/scripts/script.sh"]

# Run
ENTRYPOINT ["/scripts/llama3.sh"]
