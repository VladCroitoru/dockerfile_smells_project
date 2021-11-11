ARG BASEIMAGE=node:16.4
FROM ${BASEIMAGE}

ARG BUILD_DATE
ARG VCS_REF
ARG VERSION
LABEL mantainer="Eloy Lopez <elswork@gmail.com>" \
    org.label-schema.build-date=$BUILD_DATE \
    org.label-schema.name="cbptt" \
    org.label-schema.description="Coinbase Pro Trading Toolkit (CBPTT)" \
    org.label-schema.url="https://deft.work" \
    org.label-schema.vcs-ref=$VCS_REF \
    org.label-schema.vcs-url="https://coinbase.github.io/coinbase-pro-trading-toolkit" \
    org.label-schema.vendor="Deft Work" \
    org.label-schema.version=$VERSION \
    org.label-schema.schema-version="1.0"

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app
COPY . /usr/src/app 
RUN npm install -g ts-node 
RUN yarn add coinbase-pro-trading-toolkit
#CMD ["yarn", "test"]