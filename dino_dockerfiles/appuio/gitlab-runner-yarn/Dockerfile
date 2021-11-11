# etxend the node LTS alpine base image
FROM node:6.9-alpine

# specify the version of yarn to be installed
ENV YARN_VERSION 0.21.3
ENV YARN_DIRECTORY /opt/yarn

# install yarn
ADD https://yarnpkg.com/downloads/$YARN_VERSION/yarn-v${YARN_VERSION}.tar.gz /opt/yarn.tar.gz
RUN mkdir -p $YARN_DIRECTORY && \
    tar -xzf /opt/yarn.tar.gz -C $YARN_DIRECTORY && \
    ln -s ${YARN_DIRECTORY}/dist/bin/yarn /usr/local/bin/ && \
    rm /opt/yarn.tar.gz