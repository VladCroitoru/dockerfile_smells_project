FROM python:slim-buster

# Install git
RUN apt-get update -qq \
 && DEBIAN_FRONTEND=noninteractive apt-get -y install --no-install-recommends \
    ca-certificates \
    git \
 && apt-get autoclean && apt-get clean && apt-get -y autoremove \
 && update-ca-certificates \
 && rm -rf /var/lib/apt/lists/*

COPY subtree.sh /update-common-config/

RUN chmod +x /update-common-config/subtree.sh

ENTRYPOINT ["/update-common-config/subtree.sh"]
