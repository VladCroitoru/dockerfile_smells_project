FROM debian:buster

RUN sed -i "s/httpredir/ftp2.fr/g" /etc/apt/sources.list \
 && apt-get update -y -qq \
 && apt-get install -y -qq locales python3 python3-dev python3-venv python3-pip build-essential git \
 && apt-get remove -y -qq --purge python3-crypto \
 && rm -rf /var/lib/apt/lists/*

RUN echo 'fr_FR.UTF-8 UTF-8' > /etc/locale.gen \
 && locale-gen

ENV LANG=fr_FR.UTF-8
