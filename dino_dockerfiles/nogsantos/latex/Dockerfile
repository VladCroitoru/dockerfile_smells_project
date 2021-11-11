FROM nogsantos/ubuntu
#MAINTAINER Fabricio Nogueira nogsantos@gmail.com
LABEL Description="This image is used to compile latex documents using my default latex project base" Vendor="Nogsantos" Version="0.1.0"

RUN echo 'APT::Install-Recommends 0;' >> /etc/apt/apt.conf.d/01norecommends \
 && echo 'APT::Install-Suggests 0;' >> /etc/apt/apt.conf.d/01norecommends \
 && apt-get update \
 && DEBIAN_FRONTEND=noninteractive apt-get install -y texlive texlive-latex-base \
 texlive-humanities texlive-science texlive-lang-portuguese texlive-fonts-extra texlive-latex-extra \
 && rm -rf /var/lib/apt/lists/*

RUN mkdir -p /usr/src/project
WORKDIR /usr/src/project