FROM debian:jessie-slim

RUN apt-get update && \ 
    apt-get install -qqy apt-transport-https ca-certificates curl gnupg2 software-properties-common --no-install-recommends

# Install Docker
RUN curl -fsSL https://download.docker.com/linux/debian/gpg | apt-key add - && \
    add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/debian $(lsb_release -cs) stable" && \
    apt-get update && \
    apt-get install -qqy docker-ce

# Install Docker Compose
RUN curl -L https://github.com/docker/compose/releases/download/1.14.0/docker-compose-`uname -s`-`uname -m` > /usr/local/bin/docker-compose && \
    chmod +x /usr/local/bin/docker-compose

ENV AUTH_URL "https://gcr.io"

COPY entrypoint.sh /
RUN chmod +x /entrypoint.sh
ENTRYPOINT ["/entrypoint.sh"]
