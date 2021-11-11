FROM ubuntu:18.04

ENV TZ=Europe/Stockholm
ENV DEBIAN_FRONTEND=noninteractive

# Install packages to allow apt to use a repository over HTTPS:
RUN date && apt-get update && apt-get install -yq --no-install-recommends --fix-missing \
    apt-transport-https \
    ca-certificates \
    python3.8 \
    python3-dev \
    python3-setuptools \
    python3-pip \
    libxml2-dev \
    libxslt-dev \
    git \
    curl \
    tzdata \
    && apt-get clean && rm -rf /var/lib/apt/lists/*

RUN cp /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

# Add Docker’s official GPG key:
# RUN curl -fsSL https://download.docker.com/linux/ubuntu/gpg | apt-key add -

# Verify that you now have the key with the fingerprint, by searching for the last 8 characters of the fingerprint.
# RUN apt-key fingerprint 0EBFCD88 | grep "E2D8 8D81 803C 0EBF CD88" || exit 1

COPY . /app

WORKDIR /app

# runs unit tests with @pytest.mark.unit annotation only
RUN python3.8 -m pip install --upgrade setuptools wheel pip && \
    python3.8 -m pip install -r requirements.txt && \
    find tests -type d -name __pycache__ -prune -exec rm -rf -vf {} \; && \
    python3.8 setup.py install && \
    python3.8 -m pytest tests/unit_tests


WORKDIR /
RUN date && rm -frv /app


USER 10000
