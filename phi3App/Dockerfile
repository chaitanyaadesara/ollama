# Stage 1: Use the Ollama image from Docker Hub
FROM ollama/ollama
EXPOSE 11432
COPY phi3.sh /scripts/script.sh
RUN ["chmod", "+x", "/scripts/script.sh"]

# Run
ENTRYPOINT ["/scripts/script.sh"]