FROM node:8.9.4

RUN apt -y update && \
    apt install sudo && \
    apt install zip unzip && \
    apt install -y python-pip python-dev && \
    pip install awscli --upgrade --user && \
    export PATH=~/.local/bin:${PATH}

ENV PATH="/root/.local/bin:${PATH}"
ENTRYPOINT bash
