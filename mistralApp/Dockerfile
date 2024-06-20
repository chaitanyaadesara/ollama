# Stage 1: Use the Ollama image from Docker Hub
FROM ollama/ollama
EXPOSE 11433
COPY mistral.sh /scripts/script.sh
RUN ["chmod", "+x", "/scripts/script.sh"]

# Run
ENTRYPOINT ["/scripts/script.sh"]