FROM debian:latest

RUN apt-get update \
    && apt-get --yes install python curl unzip groff less vim jq \
    && curl "https://s3.amazonaws.com/aws-cli/awscli-bundle.zip" -o "awscli-bundle.zip" \
    && unzip awscli-bundle.zip \
    && ./awscli-bundle/install -b /bin/aws \
    && rm -rf /var/lib/apt/lists/* awscli-bundle.zip

