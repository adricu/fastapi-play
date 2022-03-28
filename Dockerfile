# [START docker]
FROM python:3.9

# Make stdout/stderr unbuffered. This prevents delay between output and cloud logging collection.
ENV PYTHONUNBUFFERED 1

# Define the port to be exposed
ENV PORT 8080

# For pipenv to set virtualenv inside project forlder
ENV PIPENV_VENV_IN_PROJECT true

# Install dependencies (if needed)
# RUN apt-get update && apt-get install -y gettext

# Set the working directory to /app
WORKDIR /app

# Copy python dependency files to /app
COPY Pipfile /app
COPY Pipfile.lock /app

# Install pipenv and requirements
RUN pip install pipenv==v2022.3.28
RUN pipenv install --deploy

# Add virtualenv bin folder to PATH
ENV PATH .venv/bin:${PATH}

# Copy the current directory contents into the container at /app
COPY . /app

# Expose port for external connections
EXPOSE ${PORT}

# Launch uvicorn
# If running behind a proxy like Nginx or Traefik add --proxy-headers
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8080", "--proxy-headers"]
# [END docker]
