FROM node:8-alpine

RUN apk --no-cache update && \
    apk --no-cache add ca-certificates groff less bash make jq curl wget g++ zip && \
    update-ca-certificates && \
    rm -rf /var/cache/apk/*

RUN apk add --no-cache python3 && \
    python3 -m ensurepip && \
    rm -r /usr/lib/python*/ensurepip && \
    pip3 install --upgrade pip setuptools && \
    if [ ! -e /usr/bin/pip ]; then ln -s pip3 /usr/bin/pip ; fi && \
    rm -r /root/.cache

WORKDIR /opt/yarn
RUN wget https://yarnpkg.com/latest.tar.gz && \
    tar zvxf latest.tar.gz && \
    rm latest.tar.gz
ENV PATH "$PATH:/opt/yarn/dist/bin"
RUN yarn --version

# Serverless framework
ENV SERVERLESS serverless@1.15.2
RUN yarn global add $SERVERLESS

# Gatsby.js framework
ENV GATSBYJS gatsby@1.9.8
RUN yarn global add $GATSBYJS

# AWS CLI
RUN pip install awscli

WORKDIR /opt/app
