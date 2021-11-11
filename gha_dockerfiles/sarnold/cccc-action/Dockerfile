FROM ubuntu:20.04

LABEL "maintainer"="Stephen Arnold <nerdboy@gentoo.org>" \
      "repository"="https://github.com/sarnold/cccc-action" \
      "homepage"="https://github.com/sarnold/cccc-action" \
      "com.github.actions.name"="cccc-action" \
      "com.github.actions.description"="Run cccc as github action" \
      "com.github.actions.icon"="check-circle" \
      "com.github.actions.color"="package"

ENV DEBIAN_FRONTEND noninteractive
# Set PYTHONUNBUFFERED so we don't get interleaved output
ENV PYTHONUNBUFFERED 1

RUN apt-get update && \
    apt-get install -y --no-install-recommends software-properties-common && \
    add-apt-repository -y -s ppa:nerdboy/embedded && \
    apt-get update && \
    apt-get install --no-install-suggests --no-install-recommends -y git cccc && \
    apt-get autoremove -y && \
    apt-get clean && \
    rm -rf /tmp/*

ADD ./src/entrypoint.py /entrypoint.py

ENTRYPOINT ["python3", "/entrypoint.py"]
