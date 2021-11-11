ARG here_version="2.4.0"

# Base image
FROM mambaorg/micromamba:latest

LABEL maintainer="Hiromu Nakamrua"
LABEL description="Micormamba container with HERE Data SDK for Python ${here_version}"
LABEL version="1.0"

# Configure Japanese environment -------------
ENV LANG ja_JP.UTF-8

USER root

RUN apt-get update && \
    apt-get install -y \
        locales \
        fonts-ipaexfont && \
    localedef -i ja_JP -c -f UTF-8 -A /usr/share/locale/locale.alias ja_JP.UTF-8 && \
    apt-get clean
# -------------------------------------------

# Copy env.yml file
COPY --chown=micromamba:micromamba env.yml /tmp/env.yml

USER micromamba

RUN micromamba install -y -n base -f /tmp/env.yml && \
    micromamba clean --all --yes && \
    mkdir /home/micromamba/.here && \
    mkdir /home/micromamba/share_w_host

COPY ./credentials/credentials.properties /home/micromamba/.here

WORKDIR /home/micromamba/share_w_host

EXPOSE 8888

CMD ["jupyter","lab","--ip=0.0.0.0","--port=8888","--no-browser"]