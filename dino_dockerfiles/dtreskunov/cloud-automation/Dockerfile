ARG TERRAFORM_VERSION=0.12.21

FROM hashicorp/terraform:${TERRAFORM_VERSION}
RUN apk update
RUN apk add \
    python3 \
    docker \
    freetype \
    graphviz \
    npm \
    ttf-opensans \
    zip
RUN pip3 install -U pip
RUN pip3 install awscli
RUN apk add \
    gcc \
    libffi-dev \
    musl-dev \
    openssl-dev \
    make \
    python3-dev
RUN pip3 install docker-compose

ENTRYPOINT []