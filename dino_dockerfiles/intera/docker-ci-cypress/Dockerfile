FROM cypress/base:12.14.0

ENV DEBIAN_FRONTEND noninteractive
ENV LANG C.UTF-8

# Update package lists and bring all package up to date.
RUN apt-get update \
    && apt-get dist-upgrade -y

# Download Cypress binary
RUN mkdir /opt/cypress \
    && curl -sS https://cdn.cypress.io/desktop/3.8.1/linux-x64/cypress.zip > /opt/cypress/cypress.zip

# Cleanup
RUN apt-get --purge -y autoremove \
	&& apt-get autoclean \
	&& apt-get clean \
	&& rm -rf /var/lib/apt/lists/*
