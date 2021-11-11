FROM ubuntu
MAINTAINER Riku Lindblad "riku.lindblad@gmail.com"

# python and relevant tools
RUN apt-get update && apt-get install -y \ 
    build-essential \
    python3 \
    python \
    python-dev \
    libxml2-dev \
    libxslt-dev \
    libssl-dev \
    zlib1g-dev \
    libyaml-dev \
    libffi-dev \
    python-pip

# General dev tools
RUN apt-get install -y git

# Latest versions of python tools via pip
RUN pip install --upgrade pip \
                          virtualenv \
                          requests
