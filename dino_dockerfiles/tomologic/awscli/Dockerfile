FROM python:3-slim

COPY requirements.txt /usr/src/app/

# Install jq and remove build-essential after pip install
RUN apt-get update && \
    apt-get install -y jq build-essential && \
    pip install --no-cache-dir -r /usr/src/app/requirements.txt && \
    apt-get remove -y --purge build-essential && \
    rm -rf /var/lib/apt/lists/*

WORKDIR /root

ENTRYPOINT [ "aws" ]
