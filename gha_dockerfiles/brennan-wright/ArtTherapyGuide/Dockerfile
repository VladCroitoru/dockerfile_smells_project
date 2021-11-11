# Use an official Python runtime as a parent image
# Use an official Python runtime based on Debian 10 "buster" as a parent image.
FROM python:3.9.7-slim-buster


# Add user that will be used in the container.
RUN useradd django

# Port used by this container to serve HTTP.
EXPOSE 8000

# Set environment variables.
# 1. Force Python stdout and stderr streams to be unbuffered.
# 2. Set PORT variable that is used by Gunicorn. This should match "EXPOSE"
#    command.
ENV PYTHONUNBUFFERED=1 \
    PORT=8000


# Install system packages required by Django.
RUN apt-get update --yes --quiet && apt-get install --yes --quiet --no-install-recommends \
    build-essential \
    libpq-dev \
    libmagic1 \
    libmariadbclient-dev \
    libjpeg62-turbo-dev \
    zlib1g-dev \
    libwebp-dev \
    && rm -rf /var/lib/apt/lists/*


COPY ./requirements.txt /code/requirements.txt

RUN pip install --upgrade pip
# Install any needed packages specified in requirements.txt
RUN pip install -r /code/requirements.txt
# Copy the current directory contents into the container at /code/
COPY . /code/

# Set the working directory to /code/
RUN mkdir -p /code/static

WORKDIR /code/

RUN chown -R django /code

RUN chmod +x /code/run_prod.sh

USER django

