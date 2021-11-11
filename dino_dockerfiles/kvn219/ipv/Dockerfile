FROM python:3.6
RUN apt-get update && apt-get install -qq -y \
    build-essential \
    libpq-dev \
    libffi-dev \
    tree \
    --no-install-recommends
# Copy ipv into the docker container's src directory
COPY . ./src/
# Install python requirements
RUN pip install -r /src/requirements.txt