FROM --platform=linux/amd64 python:3.9-slim

# Set pip to have no saved cache
ENV PIP_NO_CACHE_DIR=false

# Install poetry
RUN pip install -U poetry

# Create the working directory
WORKDIR /bot

# Install project dependencies
COPY pyproject.toml poetry.lock ./
RUN poetry config virtualenvs.create false && poetry install --no-dev --no-root

# Copy the source code in last to optimize rebuilding the image
COPY . .

ENTRYPOINT ["python3"]
CMD ["-m", "bot"]
