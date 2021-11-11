FROM alpine:latest
MAINTAINER "Mika Andrianarijaona <mikaoelitiana@gmail.com>"
RUN apk --update add git nodejs && rm -rf /var/cache/apk/* && \
    npm install -g cordova bower grunt-cli && \
    echo '{ "allow_root": true }' > /root/.bowerrc

