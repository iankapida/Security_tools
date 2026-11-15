FROM python:3.11-slim

WORKDIR /app

# Copy all repository files into the container container
COPY . /app

# Install testing dependencies
RUN pip install --no-cache-dir pytest

# Set default execution command to initialize the SIEM database
CMD ["python3", "siem_db.py"]
