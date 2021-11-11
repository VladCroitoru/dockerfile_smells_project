# Install latest version of node
FROM continuumio/anaconda3:latest

RUN apt-get update && apt-get install -y \
    build-essential \
    ca-certificates \
    curl \
    sudo \
    openssl \
    libssl-dev libffi-dev \
    --no-install-recommends

# Create directory for app
RUN mkdir /app

# Set as current directory for RUN, ADD, COPY commands
WORKDIR /app

# Add to PATH
ENV PATH /app:$PATH

# Add requirements.txt from upstream
ADD requirements.txt /app
RUN pip install -r /app/requirements.txt

# Add entire student fork (overwrites previously added package.json)
ARG SUBMISSION_SUBFOLDER
ADD $SUBMISSION_SUBFOLDER /app

# Overwrite files in student fork with upstream files
ADD test.sh /app
ADD tests /app/tests

# User defined requirements
# RUN make init