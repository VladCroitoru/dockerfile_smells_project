FROM alpine

RUN apk update && apk upgrade && \
    apk add --no-cache bash git openssh

ADD . /custom_config
ADD ./docker-start.sh /

# Mirrors the contents of the context folder to live Github content
CMD /docker-start.sh
