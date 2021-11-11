FROM alpine

MAINTAINER Chris Maki <chris.maki@ripcitysoftware.com>

ENV HOVERFLY_VERSION=v0.16.0

RUN mkdir /hoverfly

WORKDIR /hoverfly

RUN apk --no-cache add curl unzip bash

RUN mkdir -p /hoverfly/output \
 && mkdir -p /hoverfly/script

EXPOSE 8500 8888
VOLUME /hoverfly/output /hoverfly/script

RUN curl -L https://github.com/SpectoLabs/hoverfly/releases/download/${HOVERFLY_VERSION}/hoverfly_bundle_linux_amd64.zip -o /hoverfly/hoverfly.zip \
    && unzip /hoverfly/hoverfly.zip

COPY startup.sh /hoverfly/startup.sh
RUN chmod 755  /hoverfly/startup.sh


# run the script to start the app
CMD [ "/hoverfly/startup.sh" ]
