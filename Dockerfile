# Use the official Python image
FROM python:3.11-slim-bullseye

# Install git and system updates
RUN apt-get update && \
  apt-get install -y git && \
  apt-get upgrade -y && \
  apt-get autoremove -y && \
  apt-get clean && \
  rm -rf /var/lib/apt/lists/*

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV FLASK_APP=app.py
ENV FLASK_ENV=development
# Enables debug mode


# Set working directory
WORKDIR /app

# Copy project files
COPY . /app/

# Install dependencies
RUN pip install --upgrade pip && pip install -r requirements.txt

# Expose the Flask port
EXPOSE 5000

# Run the app
CMD ["python", "app.py"]