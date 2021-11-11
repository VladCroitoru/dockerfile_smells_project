FROM debian:jessie

MAINTAINER Gerco Dries <gerco@gdries.nl>

RUN apt-get update && \
    apt-get -q -y install mhonarc fontconfig libfontconfig1 libfreetype6 libpng12-0 \
                          libjpeg62-turbo openssl libX11-6 libxrender1 xfonts-base \
                          xfonts-75dpi libxext6

ADD wkhtmltox-0.12.2.1_linux-jessie-amd64.deb /
RUN dpkg -i /wkhtmltox-0.12.2.1_linux-jessie-amd64.deb 

ADD mhonarc.rc /
ADD convert.sh /

RUN mkdir /work && chown nobody: /work
USER nobody
WORKDIR /work

ENTRYPOINT ["/convert.sh"]

