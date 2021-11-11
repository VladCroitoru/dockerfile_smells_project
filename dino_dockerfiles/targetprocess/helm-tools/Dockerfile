FROM node:8-alpine

RUN apk update && apk add ca-certificates && update-ca-certificates && apk add openssl && apk add bash

#  Installing git
RUN apk update && apk upgrade && apk add --no-cache git openssh jq

#  Installing helm
WORKDIR /tools/helm

RUN wget http://storage.googleapis.com/kubernetes-helm/helm-v2.6.2-linux-amd64.tar.gz \
    && tar -xzf helm-v2.6.2-linux-amd64.tar.gz linux-amd64/helm \
    && rm helm-v2.6.2-linux-amd64.tar.gz \
    && mv ./linux-amd64/helm ./ && rm -R ./linux-amd64

ENV PATH /tools/helm:$PATH
# install yaml editor which preserve comments
RUN npm install -g yawn-yaml-cli

WORKDIR /tools

COPY ./tools/ ./
RUN find . -type f -name "*.sh" -exec chmod 755 {} \;

# Add aliases
# Use "$1" "$2" "$3" "$4" "$5" if you need to pass multi-line params like SSH key.
# Otherwise you can use $*
RUN echo -e '#!/bin/bash\n/tools/helm-package.sh $*' > /usr/bin/helm-package && \
    chmod +x /usr/bin/helm-package && \
    echo -e '#!/bin/bash\n/tools/helm-publish.sh "$1" "$2" "$3" "$4" "$5"' > /usr/bin/helm-publish && \
    chmod +x /usr/bin/helm-publish
