FROM node:8.9.4-alpine

# Install aws cli
RUN apk --update add \
    bash \
    git \
    python \
    curl \
    groff

RUN curl "https://bootstrap.pypa.io/get-pip.py" | python && \
    pip install awscli
