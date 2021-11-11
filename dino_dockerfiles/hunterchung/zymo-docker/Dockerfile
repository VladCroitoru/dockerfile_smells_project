FROM python:2
MAINTAINER Hunter Chung <hchung@zymoresearch.com>

RUN apt-get update && \
apt-get install -y \
    vim \
    wget \
    pigz \
    gcc \
    mysql-client \
    libmysqlclient-dev \
    ca-certificates \
    groff \
    less \
    curl \
    build-essential \
    libkrb5-3 \
    gfortran \
    liblapack-dev \
    libhdf5-dev \
    samtools \
    pkg-config \
    libfreetype6-dev \
    libpng-dev \
    libreadline6 \
    libreadline6-dev \
    zip \
    unzip \
    --no-install-recommends && \
rm -rf /var/lib/apt/lists/* && \
apt-get clean autoclean && \
apt-get autoremove -y

ADD install_bioinfo_packages.sh install_python_packages.sh /tmp/
RUN bash /tmp/install_bioinfo_packages.sh
RUN bash /tmp/install_python_packages.sh

ENV DJANGO_SETTINGS_MODULE=EpiQuest_py.settings \
  PYTHONPATH=${PYTHONPATH}:/usr/share/EpiQuest_py \
  TERM=xterm \
  PATH=${PATH}:/usr/share/bowtie2:/usr/share/genomicTools

VOLUME ["/usr/share/EpiQuest_py", "/mnt"]
WORKDIR /mnt
