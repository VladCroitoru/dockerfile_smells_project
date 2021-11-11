FROM node:4-slim
MAINTAINER Ryan Graham <rmg@ca.ibm.com>

# Run as unprivileged, even under docker
RUN adduser \
    --group \
    --system \
    --home /var/lib/sinopia \
    --disabled-password \
    --disabled-login \
    sinopia

USER sinopia
ENV HOME=/var/lib/sinopia

WORKDIR /var/lib/sinopia

RUN npm install --loglevel=warn --no-spin sinopia && \
    npm --no-spin --loglevel=warn cache clean && \
    rm -rf ~/.node-gyp

COPY sinopia.sh /var/lib/sinopia/run.sh

EXPOSE 4873

ENTRYPOINT ["/var/lib/sinopia/run.sh"]
