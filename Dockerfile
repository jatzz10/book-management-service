FROM python:3.12.3-slim

# Copy the latest code
WORKDIR /book-management-service
COPY . /book-management-service

# pip install required modules
RUN pip install -r requirements.txt

# Expose server port
EXPOSE 8000

# Run the script when the container starts
CMD ["/bin/bash", "docker-entrypoint.sh"]