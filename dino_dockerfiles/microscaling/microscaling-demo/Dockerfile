FROM alpine:3.4
MAINTAINER Ross Fairbanks "ross@microscaling.com"

COPY sleep.sh Dockerfile /

# Metadata params
ARG BUILD_DATE
ARG VCS_URL
ARG VCS_REF

# Metadata
LABEL org.label-schema.vendor="Microscaling Systems" \
      org.label-schema.description="Image for scaling demos from Microscaling Systems" \
      org.label-schema.license="MIT" \
      org.label-schema.url="https://microscaling.com" \
      org.label-schema.build-date=$BUILD_DATE \
      org.label-schema.vcs-url=$VCS_URL \
      org.label-schema.vcs-ref=$VCS_REF \
      org.label-schema.docker.dockerfile="/Dockerfile" \
      com.microscaling.is-scalable="True" \
      com.microscaling.priority="2" \
      com.microscaling.max-delta="2" \
      com.microscaling.min-containers="1" \
      com.microscaling.max-containers="10"

ENTRYPOINT ["/sleep.sh"]
