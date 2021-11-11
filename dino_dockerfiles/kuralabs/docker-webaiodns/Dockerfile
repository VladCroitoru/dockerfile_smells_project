FROM ubuntu:17.10
LABEL mantainer="info@kuralabs.io"

# -----

USER root
ENV DEBIAN_FRONTEND noninteractive

# Setup and install base system software
RUN echo "locales locales/locales_to_be_generated multiselect en_US.UTF-8 UTF-8" | debconf-set-selections \
    && echo "locales locales/default_environment_locale select en_US.UTF-8" | debconf-set-selections \
    && apt-get update \
    && apt-get --yes --no-install-recommends install \
        locales tzdata ca-certificates \
        bash-completion iproute2 curl nano tree \
    && rm -rf /var/lib/apt/lists/*
ENV LANG en_US.UTF-8


# Install Python stack
RUN apt-get update \
    && apt-get --yes --no-install-recommends install \
        python3 python3-dev \
        python3-pip python3-wheel python3-setuptools \
        build-essential \
    && rm -rf /var/lib/apt/lists/*


# Create user
RUN adduser \
    --system \
    --group \
    --no-create-home \
    --disabled-login \
    --uid 1010 \
    webaiodns


# Install Python modules
COPY requirements.txt /tmp/requirements.txt
RUN pip3 install --no-cache-dir -r /tmp/requirements.txt \
    && rm -rf ~/.cache/pip

# Install application
COPY webaiodns /usr/local/bin/webaiodns


WORKDIR /tmp
USER webaiodns
EXPOSE 8084/TCP
CMD webaiodns -vvv
