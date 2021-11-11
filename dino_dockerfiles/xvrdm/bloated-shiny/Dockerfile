FROM xvrdm/floating-shiny
MAINTAINER Xavier Adam <xaad@protonmail.com>

RUN apt-get update
RUN apt-get install -y --no-install-recommends \
    texlive-full
RUN apt-get install -y --no-install-recommends \
    default-jre default-jdk
RUN R CMD javareconf
