# Pull base
FROM python:3.14-slim

# Set environment variables
ENV PIP_DISABLE_PIP_VERSION_CHECK=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

# Set work directory
WORKDIR /code

# Install dependencies
COPY ./Pipfile ./Pipfile.lock ./
RUN pip install pipenv && pipenv sync --system
# Copy project 
COPY . .
