FROM python:3.9-slim

# Create app directory
WORKDIR /app

# Install poetry & disable virtual environemnt
RUN pip install poetry && \
    poetry config virtualenvs.create false

# Copy config files
COPY pyproject.toml poetry.lock ./

# Install only main dependencies
RUN poetry install --no-root --no-dev

# Copies source code
COPY src /app

# Run the app
ENTRYPOINT ["python", "/app/app.py"]
