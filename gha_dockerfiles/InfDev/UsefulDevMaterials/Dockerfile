# Install the base requirements for the app.
# This stage is to support development.

# FROM docker pull squidfunk/mkdocs-material

FROM docker pull python:3.9.7-alpine3.14 AS base
WORKDIR /tmp
COPY requirements.txt .
RUN pip install -r requirements.txt

# Set working directory
WORKDIR /docs

# Expose MkDocs development server port
EXPOSE 8000

# Start development server by default
ENTRYPOINT ["mkdocs"]
CMD ["serve", "--dev-addr=0.0.0.0:8000"]
