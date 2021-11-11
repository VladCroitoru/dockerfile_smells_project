# syntax=docker/dockerfile:1
FROM python:3.9.5

# Set pip to have no saved cache
ENV PIP_NO_CACHE_DIR=false \
    POETRY_VIRTUALENVS_CREATE=false \
    CRYPTOGRAPHY_DONT_BUILD_RUST=1

# Install poetry
RUN pip install -U poetry

# Create the working directory
WORKDIR /bot

# Install project dependencies
COPY pyproject.toml poetry.lock ./
RUN poetry install --no-dev

# Copy the source code in last to optimize rebuilding the image
COPY . .

ENTRYPOINT ["python3"]
CMD ["-m", "bot"]