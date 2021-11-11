# ==============================================================================
# Dockerfile
# ==============================================================================
FROM ruby:2.5.5-alpine
ENV LANG C.UTF-8

# Install apk package
COPY scripts/apk_install.sh scripts/apk_install.sh
RUN /bin/sh scripts/apk_install.sh

EXPOSE 3000
