FROM alpine:3.6 

MAINTAINER Minimum Builds <minumumbuilds@gmail.com>
ARG BUILD_DATE
ARG VCS_REF
LABEL Name=minimum_python3 \
      Version=0.0.8 \
      org.label-schema.build-date=$BUILD_DATE \
      org.label-schema.vcs-url="https://github.com/minimumbuilds/minimum_python3.git" \
      org.label-schema.vcs-ref=$VCS_REF
RUN apk add --update \
    python3 
