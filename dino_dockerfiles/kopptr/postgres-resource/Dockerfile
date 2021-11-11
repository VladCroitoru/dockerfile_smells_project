FROM alpine
RUN apk --update add postgresql-client jq

RUN mkdir -p /opt/resource
ADD bin/* /opt/resource/
