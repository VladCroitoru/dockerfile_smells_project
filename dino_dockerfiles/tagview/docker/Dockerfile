FROM docker:git

RUN apk add --update \
    python \
    zip \
    bash \
    && rm -rf /var/cache/apk/*

RUN curl https://s3.amazonaws.com/aws-cli/awscli-bundle.zip -o awscli-bundle.zip \
    && unzip awscli-bundle.zip \
    && ./awscli-bundle/install -i /usr/local/aws -b /usr/local/bin/aws \
    && rm -rf ./awscli-bundle \
    && rm awscli-bundle.zip
