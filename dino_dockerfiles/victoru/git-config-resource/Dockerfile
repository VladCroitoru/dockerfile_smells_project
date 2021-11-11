FROM alpine:3.6 as resource

RUN apk --no-cache add bash jq git

ADD assets/ /opt/resource/
RUN chmod +x /opt/resource/*

FROM resource AS tests
ADD test/ /tests
RUN touch ~/.gitconfig
RUN /tests/all.sh

FROM resource
